pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('test docker image build') {
      steps {
        sh 'ps aux | grep webpage.py | grep -v grep'
      }
    }

  }
}