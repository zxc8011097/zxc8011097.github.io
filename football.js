const token = '15aff59763f342bba8dd7da8782d467a';
const url = 'https://api.football-data.org/v4/matches';

async function load(){
  let dom = document.getElementById('matches');
  if(!dom) return;
  try{
    let res = await fetch(url,{headers:{'X-Auth-Token':token}});
    let data = await res.json();
    let html = '';
    (data.matches || []).slice(0,8).forEach(m=>{
      let h = m.homeTeam.name;
      let a = m.awayTeam.name;
      let s = (m.score.fullTime.homeTeam ?? '-')+' - '+(m.score.fullTime.awayTeam ?? '-');
      html+=`
      <div class="match">
        <div class="row">
          <span>${m.competition.name}</span>
          <span>${m.status=='IN_PLAY'?'直播中':'未开始'}</span>
        </div>
        <div class="teams">
          <span>${h}</span>
          <span class="score">${s}</span>
          <span>${a}</span>
        </div>
      </div>`;
    });
    dom.innerHTML = html;
  }catch(e){
    dom.innerHTML = '加载失败';
  }
}

document.addEventListener('DOMContentLoaded',load);
