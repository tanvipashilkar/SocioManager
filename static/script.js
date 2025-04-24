function connectChannel(platform) {
    fetch(`/connect/${platform}`, { method: 'POST' })
      .then(res => res.json())
      .then(data => alert(data.message));
  }
  
  function schedulePost() {
    const content = document.getElementById('content').value;
    const schedule_time = document.getElementById('schedule_time').value;
  
    fetch('/post', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content, schedule_time })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
  }
  
  function loadPosts(status) {
    fetch(`/posts/${status}`)
      .then(res => res.json())
      .then(posts => {
        let html = posts.map(p => `<div><strong>${p.content}</strong> - ${p.schedule_time}</div>`).join("");
        document.getElementById("posts-container").innerHTML = html || "No posts";
      });
  }
  
  function submitFeedback() {
    const message = document.getElementById('feedback').value;
  
    fetch('/feedback', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ feedback: message })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
  }
  