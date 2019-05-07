function doPost(e) {
  if (e == null || e.postData == null || e.postData.contents == null) {
    return;
  }
  var requestJSON = e.postData.contents;
  var requestObj = JSON.parse(requestJSON);

  var ss = SpreadsheetApp.getActive()
  var sheet = ss.getActiveSheet();

  var colNum = 5;
  var headers = sheet.getRange(150,1,1,colNum).getValues()[0];

  var values = [];
  for (i in headers){
    var header = headers[i];
    var val = "";
    switch(header) {
      case "date":
        val = new Date();
        break;
      default:
        val = requestObj[header];
        break;
    }
    values.push(val);
  }
  
  sheet.insertRowAfter(150)
  sheet.getRange(151,1,1,colNum).setValues([values]);
  
  var rowNum = sheet.getLastRow();
  
  if (rowNum > 60150) {
    sheet.deleteRow(60151);
  }
}
