var express = require('express');
var router = express.Router();
var multer  = require('multer');
var upload = multer({ dest: 'uploads/' })
var exec = require('child_process').exec;
var util = require('util');
var cmd = "/usr/local/bin/python ascii.py";

router.get('/', function(req, res, next) {
  res.render('index', { title: 'ascii.love' });
});

router.post('/upload', upload.single('image'), function(req, res, next) {
  console.log("Uploading...");
  exec(cmd + " " + req.file.path, function(error, stdout, stderr) {
    console.log("responding");
    res.status(200).send(stdout);
  });
});

module.exports = router;
