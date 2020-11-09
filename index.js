const googleTrends = require('google-trends-api');
const fs = require('fs');

googleTrends.interestOverTime({keyword: 'Trump', startTime: new Date('2017-02-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("output.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});