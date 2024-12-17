import pytest
from unittest.mock import patch, MagicMock
from masscube import untargeted_metabolomics_workflow


@pytest.fixture
def mock_environment():
    """Setup mock environment for dependencies used in the workflow."""
    with patch("src.masscube.workflows.os"), \
            patch("src.masscube.workflows.deepcopy"), \
            patch("src.masscube.workflows.multiprocessing.Pool"), \
            patch("src.masscube.workflows.time.strftime"), \
            patch("src.masscube.workflows.Params"), \
            patch("src.masscube.workflows.process_single_file"), \
            patch("src.masscube.workflows.feature_alignment"), \
            patch("src.masscube.workflows.annotate_aligned_features"), \
            patch("src.masscube.workflows.feature_annotation_mzrt"), \
            patch("src.masscube.workflows.group_features_after_alignment"), \
            patch("src.masscube.workflows.convert_signals_to_string"), \
            patch("src.masscube.workflows.convert_features_to_df"), \
            patch("src.masscube.workflows.output_feature_table"), \
            patch("src.masscube.workflows.signal_normalization"), \
            patch("src.masscube.workflows.sample_normalization"), \
            patch("src.masscube.workflows.full_statistical_analysis"), \
            patch("src.masscube.workflows.pickle.dump"), \
            patch("src.masscube.workflows.plot_ms2_matching_from_feature_table"):
        yield


def test_workflow_initialization(mock_environment):
    """Test if the workflow initializes correctly."""
    features, params = untargeted_metabolomics_workflow(path="project", return_results=True)
    assert features is not None  # Replace with expected mock behavior
    assert params is not None  # Replace with expected mock behavior