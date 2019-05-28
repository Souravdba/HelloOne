node{
 stage('SCM Checkout') {
   git 'https://github.com/Souravdba/HelloOne'
 }
 stage('Execute-shell') {
   sh 'chmod u+x ./A.sh'
   sh './A.sh'
   sh """
   virtualenv .env
   . .env/bin/activate
   pip install -r ./requirements.txt
   python ./pythontest.py
   deactivate
   """
 }
 stage('Execute-sql') {
  def retryAttempt = 0
  sh "echo 'select * from emp1' > ./aa.sql"
  retry(2) {
     if (retryAttempt > 0) {
       sleep(10 * 2 + 30 * retryAttempt)
     }

    retryAttempt = retryAttempt + 1
    sh '/opt/mssql-tools/bin/sqlcmd -S 192.168.99.100,5555 -U SA -P Password123 -d ABC -i ./aa.sql -o ./aaa.ou -e -b'
    sh 'cat ./aaa.ou'
     }
 }
 
 stage('Build status') {
   sh 'echo "Build is successfull"'
 }
}
