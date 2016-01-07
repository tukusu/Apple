var csv = require('ya-csv');
var sqlite3 = require('sqlite3');
var db = new sqlite3.Database('station.db');
var sqlInsert ='INSERT INTO station VALUES (?, ?, ?)';
var stmt = db.prepare(sqlInsert);
// equivalent of csv.createCsvFileReader('./tmp/data.csv') 
var reader = csv.createCsvFileReader('dataset/station.csv', {
    'separator': ',',
    'quote': '"',
    'escape': '"',
    'comment': '',
});
var writer = new csv.CsvWriter(process.stdout);
var i=0;
reader.addListener('data', function (data) {
	i++;
    //writer.writeRecord([data[8]]);
    stmt.run(i,data[2],data[8]);
});