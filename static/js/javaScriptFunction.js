function updateText(type) {
 var id = type+'Text';
 document.getElementById(id).value = document.getElementById(type).value;
}

function getStadium(type) {
console.log(type)
document.getElementById("city").value ='City: '+ type;
}

function checkSameTeam(type) {
var homeId=document.getElementById("homeId").value;
var awayId=document.getElementById("awayId").value;
console.log(homeId)
console.log(awayId)
if(homeId==awayId){
		window.alert("you can't select the same team");
		document.getElementById("reset").click();
	}
}

function whichTeamHasWonToss(type) {
var homeTeam=document.getElementById("homeId").value;
var awayTeam=document.getElementById("awayId").value;

for(i=document.getElementById("toss").length;i>0;i--)
{
document.getElementById("toss").remove(i);
}
var t1="";
var t2="";

if (homeTeam==="Mumbai") {
    t1="MI";
} else if (homeTeam==="Kolkata") {
    t1="KKR";
} else if (homeTeam==="Bangalore") {
    t1="RCB";
} else if (homeTeam==="Pune") {
    t1="CSK";
} else if (homeTeam==="Jaipur") {
    t1="RR";
} else if (homeTeam==="Delhi") {
    t1="DD";
} else if (homeTeam==="Dharamshala") {
    t1="KXIP";
}
else if(homeTeam==="Hyderabad"){
t1="SRH";

}

if (awayTeam==="Mumbai") {
    t2="MI";
} else if (awayTeam==="Kolkata") {
    t2="KKR";
} else if (awayTeam==="Bangalore") {
    t2="RCB";
} else if (awayTeam==="Pune") {
    t2="CSK";
} else if (awayTeam==="Jaipur") {
    t2="RR";
} else if (awayTeam==="Delhi") {
    t2="DD";
} else if (awayTeam==="Dharamshala") {
    t2="KXIP";
}
else if(awayTeam==="Hyderabad"){
t2="SRH";
}

if(t1!=""){
$(document.getElementById("toss")).append("<option value="+t1+">" +t1+ "</option>")

}
if(t2!=""){$(document.getElementById("toss")).append("<option value="+t2+">" +t2+ "</option>")
}

}
