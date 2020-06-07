pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('build docker image') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        sh 'python --version'
      }
    }

  }
}