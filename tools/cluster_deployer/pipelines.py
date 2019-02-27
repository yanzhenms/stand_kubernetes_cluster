from deployer_stages import MakeFilesDeploymentStage, BuildImageDeploymentStage, DeleteKuberDeploymentStage
from deployer_stages import TestImageDeploymentStage, PushImageDeploymentStage, PullImageDeploymentStage
from deployer_stages import DeployKuberDeploymentStage, TestKuberDeploymentStage
from deployer_stages import PushToDockerHubDeploymentStage, DeleteImageDeploymentStage

all_stages = [MakeFilesDeploymentStage,
              DeleteImageDeploymentStage,
              BuildImageDeploymentStage,
              TestImageDeploymentStage,
              PushImageDeploymentStage,
              PullImageDeploymentStage,
              DeleteKuberDeploymentStage,
              DeployKuberDeploymentStage,
              TestKuberDeploymentStage,
              PushToDockerHubDeploymentStage]

preset_pipelines = {
    'all': {
        'description': 'full cycle deployment: from making deploying files up to pushing to Docker Hub',
        'pipeline': [MakeFilesDeploymentStage,
                     DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     TestImageDeploymentStage,
                     PushImageDeploymentStage,
                     DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage,
                     TestKuberDeploymentStage,
                     PushToDockerHubDeploymentStage]
    },
    'all_up_kuber': {
        'description': 'full cycle deployment without pushing to Docker Hub',
        'pipeline': [MakeFilesDeploymentStage,
                     DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     TestImageDeploymentStage,
                     PushImageDeploymentStage,
                     DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage,
                     TestKuberDeploymentStage]
    },
    'all_up_kuber_no_tests': {
        'description': 'full cycle deployment without pushing to Docker Hub without tests',
        'pipeline': [MakeFilesDeploymentStage,
                     DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     PushImageDeploymentStage,
                     DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage]
    },
    'all_from_docker': {
        'description': 'full cycle deployment without making deployment files',
        'pipeline': [DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     TestImageDeploymentStage,
                     PushImageDeploymentStage,
                     DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage,
                     TestKuberDeploymentStage,
                     PushToDockerHubDeploymentStage]
    },
    'from_docker_up_kuber': {
        'description': 'deployment cycle from building images up to deploying in Kubernetes',
        'pipeline': [DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     TestImageDeploymentStage,
                     PushImageDeploymentStage,
                     DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage,
                     TestKuberDeploymentStage]
    },
    'make_files': {
        'description': 'make deployment files',
        'pipeline': [MakeFilesDeploymentStage]
    },
    'build_docker': {
        'description': 'build and test images',
        'pipeline': [DeleteImageDeploymentStage,
                     BuildImageDeploymentStage,
                     TestImageDeploymentStage]
    },
    'build_docker_no_tests': {
        'description': 'build images without tests',
        'pipeline': [DeleteImageDeploymentStage,
                     BuildImageDeploymentStage]
    },
    'delete_docker': {
        'description': 'delete docker images',
        'pipeline': [DeleteImageDeploymentStage]
    },
    'create_kuber': {
        'description': 'deploy in Kubernetes and test',
        'pipeline': [DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage,
                     TestKuberDeploymentStage]
    },
    'create_kuber_no_tests': {
        'description': 'deploy in Kubernetes without test',
        'pipeline': [DeleteKuberDeploymentStage,
                     DeployKuberDeploymentStage]
    },
    'delete_kuber': {
        'description': 'delete Kubernetes deployment',
        'pipeline': [DeleteKuberDeploymentStage]
    },
    'push_to_registry': {
        'description': 'push images to local registry',
        'pipeline': [PushImageDeploymentStage]
    },
    'pull_from_registry': {
        'description': 'push images from local registry',
        'pipeline': [PullImageDeploymentStage]
    },
    'push_to_docker_hub': {
        'description': 'push images to Docker Hub',
        'pipeline': [PushToDockerHubDeploymentStage]
    }
}
