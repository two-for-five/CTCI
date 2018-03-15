function longestWord(sen){
  sen = sen.toLowerCase().match(/[a-z0-9]+/g);
  sen.sort(function(a, b){
    return b.length - a.length;
  })
  const result = sen.filter(word => word.length === sen[0].length);
  if (result.length == 1){
    return result[0];
  }
  else{
    return result;
  }
}
//console.log(longestWord("hello, there my name is brad"));

function chunkArray(arr, len){
  result = []
  let i = 0;
  while (i < arr.length){
    result.push(arr.slice(i, i + len));
    i = i + len;
  }
  return result;
}
//console.log(chunkArray([1,2,3,4,5,6,7], 3));
function flattenArray(arrays){
  return arrays.reduce((res,numArray) => res.concat(numArray) ,[])
}
// console.log(flattenArray([ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7 ] ]));

function formatStr(str){
  return str.replace(/[^\w]/g, "").toLowerCase().split('').sort().join('');
}
function isAnagram(str1, str2){
  return formatStr(str1) === formatStr(str2);
}
console.log(isAnagram("elbow", "below"));
