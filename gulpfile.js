const gulp = require('gulp');
const shell = require('gulp-shell');

const create_virtual_environment = [
  'virtualenv -p python3 .virtual\n',
  'source .virtual/bin/activate && pip install -r requirements.txt && deactivate\n'
];

const create_local_runtime_variables = [
  'cp ./env/local .env\n'
];

gulp.task('install', shell.task([].concat(
  create_virtual_environment,
  create_local_runtime_variables
).join('')));

gulp.task('pip', shell.task((function pip(){
  if(process.argv[3]=='-i'){
    return 'source .virtual/bin/activate && pip install '
      +process.argv[4] + ' && pip freeze > requirements.txt && deactivate';
  }
}())));

gulp.task('tr', shell.task([
  'export $(cat .env | xargs) && .virtual/bin/coverage run --source=src -m unittest discover -s src\n',
  '.virtual/bin/coverage html\n'
].join('')));


// TODO rebuild .env gulp file

//gulp env


gulp.task('env', shell.task([].concat(
  create_local_runtime_variables
).join('')));



/**
 * 
 * Important testing setup
 */
// New test runner ()
// local test runner
// the idea for above should be
// create a different ( docker-compose file for testing ) run docker-copose up with a testing environment. ( this will just tell the application to use the test datbase )
// wipe database
// run seed script
// integration test `newman run ./postman/flask.postman_collection.json`


gulp.task('newman', shell.task([].concat(
  ['newman run ./postman/flask.postman_collection.json']
).join('')));


gulp.task('w', function(){
  gulp.watch('src/**/*.py', ['tr'])
});

