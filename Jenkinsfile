node{
 stage('SCM Checkout') {
   git 'https://github.com/Souravdba/HelloOne'
 }
 stage('Execute') {
   sh 'chmod u+x ./A.sh'
   sh './A.sh'
   sh 'python ./pythontest.py'
 }
 stage('Execute-test') {
  def retryAttempt = 0
  sh "echo 'select * from location' > ./aa.sql"
  retry(2) {
     if (retryAttempt > 0) {
       sleep(1000 * 2 + 2000 * retryAttempt)
     }

    retryAttempt = retryAttempt + 1
    sh '/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Welcome123 -d TestDB -i ./aa.sql -o ./aaa.ou -e'
    sh 'cat ./aaa.ou'
     }
 }
 
 stage('Build status') {
   sh 'echo "Build is successfull"'
 }
}
