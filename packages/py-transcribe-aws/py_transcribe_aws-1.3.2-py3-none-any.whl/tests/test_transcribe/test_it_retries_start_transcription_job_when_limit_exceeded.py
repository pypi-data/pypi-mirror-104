#
# This software is Copyright ©️ 2020 The University of Southern California. All Rights Reserved.
# Permission to use, copy, modify, and distribute this software and its documentation for educational, research and non-profit purposes, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and subject to the full license file found in the root of this software deliverable. Permission to make commercial use of this software may be obtained by contacting:  USC Stevens Center for Innovation University of Southern California 1150 S. Olive Street, Suite 2300, Los Angeles, CA 90115, USA Email: accounting@stevens.usc.edu
#
# The full terms of this copyright and license should always be found in the root directory of this software deliverable as "license.txt" and if these terms are not found with this software, please contact the USC Stevens Center for the full license.
#
import pytest
from unittest.mock import patch

from transcribe import (
    TranscribeBatchResult,
    TranscribeJob,
    TranscribeJobRequest,
    TranscribeJobStatus,
    TranscribeJobsUpdate,
)

from transcribe_aws import DEFAULT_POLL_INTERVAL

from .helpers import (
    raise_limit_exceeded,
    run_transcribe_test,
    AwsTranscribeGetJobCall,
    AwsTranscribeListJobsCall,
    AwsTranscribeStartJobCall,
    TranscribeTestFixture,
    TEST_AWS_REGION,
    TEST_TRANSCRIBE_SOURCE_BUCKET,
)


@patch("boto3.client")
@pytest.mark.parametrize(
    "fixture",
    [
        (
            TranscribeTestFixture(
                batch_id="b1",
                requests=[
                    TranscribeJobRequest(jobId="m1-u1", sourceFile="/audio/m1/u1.wav"),
                    TranscribeJobRequest(jobId="m1-u2", sourceFile="/audio/m1/u2.wav"),
                    TranscribeJobRequest(jobId="m1-u3", sourceFile="/audio/m1/u3.wav"),
                ],
                override_expected_start_job_calls=[
                    AwsTranscribeStartJobCall(
                        expected_args={
                            "TranscriptionJobName": "b1-m1-u1",
                            "LanguageCode": "en-US",
                            "Media": {
                                "MediaFileUri": f"https://s3.{TEST_AWS_REGION}.amazonaws.com/{TEST_TRANSCRIBE_SOURCE_BUCKET}/b1-m1-u1.wav"
                            },
                            "MediaFormat": "wav",
                        }
                    ),
                    AwsTranscribeStartJobCall(
                        expected_args={
                            "TranscriptionJobName": "b1-m1-u2",
                            "LanguageCode": "en-US",
                            "Media": {
                                "MediaFileUri": f"https://s3.{TEST_AWS_REGION}.amazonaws.com/{TEST_TRANSCRIBE_SOURCE_BUCKET}/b1-m1-u2.wav"
                            },
                            "MediaFormat": "wav",
                        }
                    ),
                    AwsTranscribeStartJobCall(
                        expected_args={
                            "TranscriptionJobName": "b1-m1-u3",
                            "LanguageCode": "en-US",
                            "Media": {
                                "MediaFileUri": f"https://s3.{TEST_AWS_REGION}.amazonaws.com/{TEST_TRANSCRIBE_SOURCE_BUCKET}/b1-m1-u3.wav"
                            },
                            "MediaFormat": "wav",
                        },
                        side_effect=raise_limit_exceeded,
                    ),
                    AwsTranscribeStartJobCall(
                        expected_args={
                            "TranscriptionJobName": "b1-m1-u3",
                            "LanguageCode": "en-US",
                            "Media": {
                                "MediaFileUri": f"https://s3.{TEST_AWS_REGION}.amazonaws.com/{TEST_TRANSCRIBE_SOURCE_BUCKET}/b1-m1-u3.wav"
                            },
                            "MediaFormat": "wav",
                        }
                    ),
                ],
                list_jobs_calls=[
                    AwsTranscribeListJobsCall(
                        result={
                            "TranscriptionJobSummaries": [
                                {
                                    "TranscriptionJobName": "b1-m1-u1",
                                    "TranscriptionJobStatus": "QUEUED",
                                }
                            ]
                        }
                    ),
                    AwsTranscribeListJobsCall(
                        result={
                            "TranscriptionJobSummaries": [
                                {
                                    "TranscriptionJobName": "b1-m1-u1",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u2",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                            ]
                        }
                    ),
                    AwsTranscribeListJobsCall(
                        result={
                            "TranscriptionJobSummaries": [
                                {
                                    "TranscriptionJobName": "b1-m1-u1",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u2",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u3",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                            ]
                        }
                    ),
                    AwsTranscribeListJobsCall(
                        result={
                            "TranscriptionJobSummaries": [
                                {
                                    "TranscriptionJobName": "b1-m1-u1",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u2",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u3",
                                    "TranscriptionJobStatus": "QUEUED",
                                },
                            ]
                        }
                    ),
                    AwsTranscribeListJobsCall(
                        result={
                            "TranscriptionJobSummaries": [
                                {
                                    "TranscriptionJobName": "b1-m1-u1",
                                    "TranscriptionJobStatus": "COMPLETED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u2",
                                    "TranscriptionJobStatus": "COMPLETED",
                                },
                                {
                                    "TranscriptionJobName": "b1-m1-u3",
                                    "TranscriptionJobStatus": "COMPLETED",
                                },
                            ]
                        }
                    ),
                ],
                get_job_calls=[
                    AwsTranscribeGetJobCall(
                        name="b1-m1-u1",
                        result={
                            "TranscriptionJob": {
                                "TranscriptionJobStatus": "COMPLETED",
                                "Transcript": {
                                    "TranscriptFileUri": "http://fake/b1-m1-u1"
                                },
                            }
                        },
                        transcribe_url_response={
                            "results": {
                                "transcripts": [
                                    {
                                        "transcript": "transcript for mentor m1 and utterance u1"
                                    }
                                ]
                            }
                        },
                    ),
                    AwsTranscribeGetJobCall(
                        name="b1-m1-u3",
                        result={
                            "TranscriptionJob": {
                                "TranscriptionJobStatus": "COMPLETED",
                                "Transcript": {
                                    "TranscriptFileUri": "http://fake/b1-m1-u3"
                                },
                            }
                        },
                        transcribe_url_response={
                            "results": {
                                "transcripts": [
                                    {
                                        "transcript": "transcript for mentor m1 and utterance u2"
                                    }
                                ]
                            }
                        },
                    ),
                    AwsTranscribeGetJobCall(
                        name="b1-m1-u2",
                        result={
                            "TranscriptionJob": {
                                "TranscriptionJobStatus": "COMPLETED",
                                "Transcript": {
                                    "TranscriptFileUri": "http://fake/b1-m1-u2"
                                },
                            }
                        },
                        transcribe_url_response={
                            "results": {
                                "transcripts": [
                                    {
                                        "transcript": "transcript for mentor m1 and utterance u3"
                                    }
                                ]
                            }
                        },
                    ),
                ],
                expected_sleep_calls=[DEFAULT_POLL_INTERVAL, DEFAULT_POLL_INTERVAL],
                expected_result=TranscribeBatchResult(
                    transcribeJobsById={
                        "b1-m1-u1": TranscribeJob(
                            batchId="b1",
                            jobId="m1-u1",
                            sourceFile="/audio/m1/u1.wav",
                            mediaFormat="wav",
                            status=TranscribeJobStatus.SUCCEEDED,
                            transcript="transcript for mentor m1 and utterance u1",
                        ),
                        "b1-m1-u2": TranscribeJob(
                            batchId="b1",
                            jobId="m1-u2",
                            sourceFile="/audio/m1/u2.wav",
                            mediaFormat="wav",
                            status=TranscribeJobStatus.SUCCEEDED,
                            transcript="transcript for mentor m1 and utterance u2",
                        ),
                        "b1-m1-u3": TranscribeJob(
                            batchId="b1",
                            jobId="m1-u3",
                            sourceFile="/audio/m1/u3.wav",
                            mediaFormat="wav",
                            status=TranscribeJobStatus.SUCCEEDED,
                            transcript="transcript for mentor m1 and utterance u3",
                        ),
                    }
                ),
                expected_on_update_calls=[
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.UPLOADED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u1"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u1"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.UPLOADED,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u2"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.NONE,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u2"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.UPLOADED,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u3"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.QUEUED,
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u3"],
                    ),
                    TranscribeJobsUpdate(
                        result=TranscribeBatchResult(
                            transcribeJobsById={
                                "b1-m1-u1": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u1",
                                    sourceFile="/audio/m1/u1.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.SUCCEEDED,
                                    transcript="transcript for mentor m1 and utterance u1",
                                ),
                                "b1-m1-u2": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u2",
                                    sourceFile="/audio/m1/u2.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.SUCCEEDED,
                                    transcript="transcript for mentor m1 and utterance u2",
                                ),
                                "b1-m1-u3": TranscribeJob(
                                    batchId="b1",
                                    jobId="m1-u3",
                                    sourceFile="/audio/m1/u3.wav",
                                    mediaFormat="wav",
                                    status=TranscribeJobStatus.SUCCEEDED,
                                    transcript="transcript for mentor m1 and utterance u3",
                                ),
                            }
                        ),
                        idsUpdated=["b1-m1-u1", "b1-m1-u2", "b1-m1-u3"],
                    ),
                ],
            )
        )
    ],
)
def test_it_retries_start_transcription_job_when_limit_exceeded(
    mock_boto3_client, fixture: TranscribeTestFixture
):
    run_transcribe_test(mock_boto3_client, fixture)
