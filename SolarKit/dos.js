var config = require('./dos_conf.json');

var Stress = require('ddos-stress');

var stress = new Stress();

stress.run(config['server'], config['requests'], config['port'])