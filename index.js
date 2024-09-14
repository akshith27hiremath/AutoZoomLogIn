while (true){
    numberOfPeriods = prompt('Enter number of periods per day: ')
    if (!(isNaN(parseInt(numberOfPeriods)))) {
        break;
    }
}
numberOfPeriods = parseInt(numberOfPeriods)
numberOfDays = 0;
while (true){
    numberOfDays = prompt('Enter number of days: ')
    if (!(isNaN(parseInt(numberOfDays)))) {
        break;
    }
}
numberOfDays = parseInt(numberOfDays)
alert('Now enter each day in order in the format Monday/Tuesday/Wednesday/Thursday/Friday, or Wednesday/Thursday/Friday etc')
x = 0
while (true){
    days = prompt("Enter the days in order, separated by a '/'")
    days = days.split("/");
    for (let index = 0; index < days.length; index++) {
        const day = days[index];
        if (day == 'Monday' || day == 'Tuesday' || day == 'Wednesday' || day == 'Thursday' || day == 'Friday' || day == 'Saturday' || day == 'Sunday'){
            x++;
        }
    }
    if (x == numberOfDays) {
        break;
    } else {
        alert('Please use the correct format and spelling.')
        x = 0;
    }
}
alert('You can now fill in the timetable.')
numberOfRows = numberOfDays * numberOfPeriods
x = 1
y=1
z=0
//x=row
//y=period
//z=day
tableContent = ""
timingsContent = ""
period = 1
while(period<=numberOfPeriods){
    timingsContent = timingsContent +  `<tr><td>${period}</td><td><form class="ui form"><input type="time" id=${period}-start></form></td><td><form class="ui form"><input type="time" id=${period}-end></form></td></tr>`
    period++
}
document.getElementById("main_content_timings").innerHTML = timingsContent
console.log(numberOfPeriods)
while(x<=numberOfRows) {
    day = days[z]
    bg_colours = ["#baffcd","#d3d3d3","#add8e6","#ffbaba","#CDCDCD","#faffba","#afeeee"]
    row = `<tr style="background-color:${bg_colours[z]};"><td>${day}</td><td>${y}</td><td><form class="ui form"><input type="text" name="${day}-${y}-id" id="${day}-${y}-id" required placeholder="Meeting ID"></form></td><td><form class="ui form"><input type="text" name="${day}-${y}-pwd" id="${day}-${y}-pwd" required placeholder="Password"></form></td></tr>`
    tableContent = tableContent + row
    x++;
    y++;
    if(y>numberOfPeriods) {
        y=1;
        z++;
    }
}
tbody = document.getElementById("main_content")
tbody.innerHTML = tableContent
ids_passwords_input_names = []
ids_passwords_text = `"meetingids":{"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[]`
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []
sunday = []
timing_json_text = ""
function getAll(){
    getTimings()
}
function formatTime(org){
    if (org[0] == "0") {
        return org[1]+org[3]+org[4]
    } else {
        return org[0]+org[1]+org[3]+org[4]
    }
}
function getTimings() {
    var period = 1
    while (period<=numberOfPeriods) {
        start_time = parseInt(formatTime(document.getElementById(`${period}-start`).value))
        end_time = parseInt(formatTime(document.getElementById(`${period}-end`).value))
        text = `"${period}": [${start_time}, ${end_time}],`
        timing_json_text = `${timing_json_text}${text}`
        console.log(text)
        period++
    }
    timing_json_text = timing_json_text.slice(0,-1)
    getIDS()
}
function getIDS(){
    period = 1
    days.forEach(day => {
        while (period<=numberOfPeriods){
            id_name = `${day}-${period}-id`
            pwd_name = `${day}-${period}-pwd`
            ids_passwords_input_names.push([id_name, pwd_name])
            period++
        }
        period = 1
    });
    ids_passwords_input_names.forEach(id_password_name => {
        day = id_password_name[0].split("-")[0]
        meeting_id = document.getElementById(id_password_name[0]).value
        pwd = document.getElementById(id_password_name[1]).value
        text = ['x', meeting_id, pwd]
        if (day=='Monday') {
            day = '1'
            monday.push(text)
        } else if (day=='Tuesday') {
            day='2'
            tuesday.push(text)
        } else if (day=='Wednesday') {
            day='3'
            wednesday.push(text)
        } else if (day=='Thursday') {
            day='4'
            thursday.push(text)
        } else if (day=='Friday') {
            day='5'
            friday.push(text)
        } else if (day=='Saturday') {
            day='6'
            saturday.push(text)
        } else if (day=='Sunday') {
            day='7'
            sunday.push(text)
        } 
    });
    monday_json = JSON.stringify(monday)
    tuesday_json = JSON.stringify(tuesday)
    wednesday_json = JSON.stringify(wednesday)
    thursday_json = JSON.stringify(thursday)
    friday_json = JSON.stringify(friday)
    saturday_json = JSON.stringify(saturday)
    sunday_json = JSON.stringify(sunday)
    ids_passwords_text = `"meetingids":{"1":${monday_json},"2":${tuesday_json},"3":${wednesday_json},"4":${thursday_json},"5":${friday_json},"6":${saturday_json},"7":${sunday_json}}`
    done()
}

final_json = ""
function done(){
    final_json = `{"timedivisions": {${timing_json_text}},${ids_passwords_text}}`
    downloadToFile(final_json, 'timetable.json', 'text/plain');
    document.querySelector("body").innerHTML = `<div style="font-family:monospace"><h1 class="ui header huge" style="text-align: center; margin: 2.5rem;">Copy the downloaded file to the same directory as the exe file.</h1></div>`
}
const downloadToFile = (content, filename, contentType) => {
    const a = document.createElement('a');
    const file = new Blob([content], {type: contentType});
    
    a.href= URL.createObjectURL(file);
    a.download = filename;
    a.click();
  
      URL.revokeObjectURL(a.href);
};
