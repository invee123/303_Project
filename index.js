const googleTrends = require('google-trends-api');
const fs = require('fs');

googleTrends.interestOverTime({keyword: 'Trump', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_trump.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});

googleTrends.interestOverTime({keyword: 'Raise Taxes', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_tax.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});

googleTrends.interestOverTime({keyword: 'google', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_google.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});

googleTrends.interestOverTime({keyword: 'youtube', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_youtube.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});

googleTrends.interestOverTime({keyword: 'amazon', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_amazon.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});

googleTrends.interestOverTime({keyword: 'android', startTime: new Date('2016-01-01'), granularTimeResolution: true})
.then(function(results){
  fs.writeFile("trend_android.txt", results, function(err) {
      if(err) {
          return console.log(err);
      }
      console.log("The file was saved!");
  }); 
})
.catch(function(err){
  console.error('Couldn\'t read trends', err);
});