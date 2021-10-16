System.register(["./chunk-vendor.js","./chunk-tip.js","./chunk-line.js","./chunk-frameworks.js"],(function(){"use strict";var t,a,e,s,r,n,o,i,c,l,d,u,p,f,m,h;return{setters:[function(s){t=s._,a=s.t,e=s.c},function(t){s=t.z,r=t.s,n=t.m,o=t.h,i=t.g,c=t.j},function(t){l=t.u,d=t.r,u=t.j,p=t.t,f=t.l},function(t){m=t.m,h=t.aY}],execute:function(){const g=m((async function(t){const a=await h(t,{headers:{accept:"application/json"}});return await a.json()}));let y=class CommunityContributionsGraphElement extends HTMLElement{async connectedCallback(){const t=this.graph,a=t.getAttribute("data-url");if(a){for(const a of t.querySelectorAll("svg.viz"))a.remove();t.classList.add("is-graph-loading"),t.classList.remove("is-graph-load-error","is-graph-empty");try{const e=await g(a);t.classList.remove("is-graph-loading"),e&&function(t){const a=t.clientWidth,e=t.clientHeight,m={top:50,right:20,bottom:40,left:50},h=a-m.left-m.right,g=e-m.top-m.bottom,y=l("%B %-d %Y"),x=l("%-m/%-d"),v=function(){const t=[{class:"discussions-line",name:"discussions",delta:0,data:[]},{class:"issues-line",name:"issues",delta:100,data:[]},{class:"pull-requests-line",name:"pull requests",delta:170,data:[]}];for(let a=0;a<31;a++)for(const e of t)e.data.push({date:new Date(Date.now()+24*a*60*60*1e3),value:Math.floor(100*Math.random()),type:e.name});for(const a of t){const t=[];for(const[e,s]of a.data.entries())e%7==0&&t.push({date:s.date,value:0,type:null}),t[t.length-1].value+=s.value;a.data=t}return t}(),k=s().attr("class","svg-tip").offset([-10,0]).html((function(t){return`<strong>${y(t.date)}</strong><br> ${t.value} created`})),b=r(t).append("svg").attr("class","viz").attr("width",a).attr("height",e).attr("alt","A graph of added discussions, issues, and pull requests on this repository").attr("aria-describedby","community-contributions-description").append("g").attr("transform",`translate(${m.left},${m.top})`).call(k);let w="";for(const s of v){w+=s.name+": ";for(const t of s.data)w+=`${t.value} on ${x(t.date)} `}b.append("div").attr("text",w).attr("style","display: none;").attr("id","community-contributions-description");for(const s of v)b.append("line").attr("x1",m.right+s.delta).attr("y1",-m.top/2).attr("x2",m.right+16+s.delta).attr("y2",-m.top/2).attr("class",s.class),b.append("text").attr("x",m.right+21+s.delta).attr("y",-m.top/2+5).attr("class","legend-text").text(s.name);const[j,$]=d(v[0].data,(t=>t.date));let z=0;for(const s of v)z=Math.max(n(s.data,(t=>t.value))||-1/0,z);const L=v[0].data.map((t=>t.date)),S=u().domain([j,$]).range([0,h]);b.append("g").attr("transform",`translate(0, ${g})`).attr("class","tick-labels-x").call(o(S).tickSize(0).tickValues(L).tickFormat(p("%-m/%-d")));const q=i().domain([0,z]).range([g,0]);b.append("g").attr("class","tick-labels-y").call(c(q).ticks(4).tickSize(0)),b.append("g").attr("class","tick-y").call(c(q).ticks(4).tickSize(-h).tickFormat((()=>""))),b.append("g").attr("class","tick-x").attr("transform",`translate(0,${g})`).call(o(S).tickValues(L.slice(0,-1)).tickSize(-g).tickFormat((()=>""))),b.append("text").attr("class","axis-label").attr("text-anchor","middle").attr("x",h/2).attr("y",e-m.top).text("Timeline"),b.append("text").attr("class","axis-label").attr("transform","rotate(-90)").attr("x",-g/2).attr("y",-m.bottom-10).attr("dy","0.71em").style("text-anchor","middle").text("Quantity");for(const s of v)b.append("path").datum(s.data).attr("class",s.class).attr("d",f().x((function(t){return S(t.date)})).y((function(t){return q(t.value)})));for(const s of v)b.append("g").selectAll("dot").data(s.data).enter().append("circle").attr("cx",(function(t){return S(t.date)})).attr("cy",(function(t){return q(t.value)})).attr("r",5).attr("class",s.class).on("mouseover",k.show).on("mouseout",k.hide)}(t)}catch(e){throw t.classList.remove("is-graph-loading"),t.classList.add("is-graph-load-error"),e}}}};t([a],y.prototype,"graph",void 0),y=t([e],y)}}}));
//# sourceMappingURL=chunk-community-contributions-57ecfb03.js.map
