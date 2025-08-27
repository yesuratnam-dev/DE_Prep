"""Unit tests for data ingestion."""

import pytest
import json
from unittest.mock import patch, MagicMock
from scripts.ingest_data import ingest_fda_data

@pytest.fixture
def mock_fda_response():
    return {
        "results": [
            {
                "drug_name": "Test Drug",
                "manufacturer_name": "Test Manufacturer",
                "status": "Active",
                "shortage_reason": "Manufacturing delay"
            }
        ]
    }

@patch('scripts.ingest_data.boto3.client')
@patch('scripts.ingest_data.requests.get')
def test_ingest_fda_data_success(mock_get, mock_boto3, mock_fda_response):
    # Mock API response
    mock_response = MagicMock()
    mock_response.json.return_value = mock_fda_response
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    # Mock S3 client
    mock_s3 = MagicMock()
    mock_boto3.return_value = mock_s3
    
    # Test ingestion
    result = ingest_fda_data("2024-01-01")
    
    assert result is True
    mock_s3.put_object.assert_called_once()

@patch('scripts.ingest_data.requests.get')
def test_ingest_fda_data_api_failure(mock_get):
    # Mock API failure
    mock_get.side_effect = Exception("API Error")
    
    # Test ingestion
    result = ingest_fda_data("2024-01-01")
    
    assert result is False
