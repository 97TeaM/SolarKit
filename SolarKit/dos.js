const config = require('./dos_conf.json');

const Stress = require('ddos-stress');

const stress = new Stress()

stress.run(config['web-site'], config['requests'])