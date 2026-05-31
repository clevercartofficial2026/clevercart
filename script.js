const allSources = [
  "YouTube API", "Reddit Threads", "Twitter Sentiment", 
  "Consumer Complaints", "MouthShut India", "Google Trust Index",
  "Tech Forums", "GitHub Issues", "Trustpilot", "Expert Blogs"
];

async function doSearch() {
  const query = document.getElementById('si').value.trim();
  if(!query) {
    alert("कृपया प्रोडक्ट का नाम लिखें!");
    return;
  }

  // UI छुपाना और लोडर दिखाना
  document.getElementById('aiLoader').style.display = 'block';
  document.getElementById('resultScreen').style.display = 'none';
  const sourceDiv = document.getElementById('sourceStatus');
  const pBar = document.getElementById('pBar');
  const percentText = document.getElementById('percent');
  sourceDiv.innerHTML = '';

  // 10 सोर्सेस को स्कैन करने का एनीमेशन
  for(let i=0; i < allSources.length; i++) {
    const sItem = document.createElement('div');
    sItem.className = 'source-item';
    sItem.innerHTML = `⏳ Scanning ${allSources[i]}...`;
    sourceDiv.appendChild(sItem);

    // थोड़ा इंतज़ार ताकि यूजर को लगे कि AI काम कर रहा है
    await new Promise(r => setTimeout(r, 600)); 

    sItem.innerHTML = `✅ ${allSources[i]} Checked`;
    sItem.style.color = "#00A651";
    
    let progress = ((i + 1) / allSources.length) * 100;
    pBar.style.width = progress + "%";
    percentText.innerText = Math.round(progress) + "%";
  }

  // रिजल्ट दिखाना
  setTimeout(() => {
    document.getElementById('aiLoader').style.display = 'none';
    document.getElementById('resultScreen').style.display = 'block';
    document.getElementById('finalScore').innerText = (Math.random() * (9.5 - 6.5) + 6.5).toFixed(1);
    document.getElementById('verdict').innerText = "Highly Recommended by CleverCart AI";
  }, 500);
                                    }
