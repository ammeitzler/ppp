var lines;
var json_file;

function preload() {
  //lines = loadStrings("testdata.txt");
  //console.log(lines)
}

function setup() {
  json_file = loadJSON("json_data.json", drawData);
  canvas_width = 1100;
  canvas_height = 600;
  createCanvas(1100, 600);
  textSize(20);
  fill(0);
  noLoop();
}

function draw() {
  // for (var i=0; i<lines.length; i++) {
  //   text(lines[i], 5, 20*i+20);
  // }
}

function drawData(data) {
	console.log(json_file)
	console.log(json_file.sentences)
	json_file_length = json_file.sentences.length
	random_num = Math.round(Math.random() * (json_file_length  - 0) + 0);

	console.log(random_num)
	text(json_file.noun[random_num],canvas_width%random(width) ,random(height))
	text(json_file.sentences[random_num],canvas_width%random(width) ,canvas_height%random(height))
	//text(json_file.punct.join(""),50 ,50)

	for(i = 0; i< json_file.punct.length%random_num; i++) {
		text(json_file.punct[i],canvas_width%random(width),random(height)-30)
	}
	//line(random_num*50, 0, 100, 0);
	line(random_num*50, 5, random_num*50, 200)
	line(50, random_num*20, random_num*10, random_num*20)
}




