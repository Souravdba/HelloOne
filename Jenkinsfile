node{
 stage('SCM Checkout') {
   git 'https://github.com/Souravdba/HelloOne'
 }
 stage('Execute') {
   sh 'chmod u+x ./A.sh'
   sh './A.sh'
 }
 
 stage('Build status') {
   sh 'echo "Build is successfull"'
 }
}
