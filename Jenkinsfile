node{
 stage('SCM Checkout') {
   git 'https://github.com/Souravdba/HelloOne'
 }
 state('Execute') {
   sh 'A.sh'
 }
 
 state('Build status') {
   sh 'echo "Build is successfull"'
 }
}