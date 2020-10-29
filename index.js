const googleTrends = require('google-trends-api');

googleTrends.interestOverTime({keyword: 'Trump', startTime: new Date('2017-02-01'), granularTimeResolution: true})
.then(function(results){
  console.log('These results are awesome', results);
})
.catch(function(err){
  console.error('Oh no there was an error', err);
});