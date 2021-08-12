function uploadFile(form)
{
 console.log(form)
 alert(document.getElementById("file").value)
 const formData = new FormData(form);
 var oOutput = document.getElementById("static_file_response")
 var oReq = new XMLHttpRequest();
     oReq.open("POST", "upload_static_file", true);
 oReq.onload = function(oEvent) {
     if (oReq.status == 200) {
       oOutput.innerHTML = "Uploaded!";
       console.log(oReq.response)
     } else {
       oOutput.innerHTML = "Error occurred when trying to upload your file.<br>";
     }
     };
 oOutput.innerHTML = "Sending file!";
 console.log("Sending file!")
 oReq.send(formData);
}