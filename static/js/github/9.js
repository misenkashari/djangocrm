System.register(["./chunk-frameworks.js","./chunk-vendor.js"],(function(){"use strict";var e,t,r,n;return{setters:[function(r){e=r.C,t=r.o},function(e){r=e.a,n=e.o}],execute:function(){function c(){const e=Array.from(document.querySelectorAll("input[type=text].js-advanced-search-prefix")),t=Array.from(document.querySelectorAll("select.js-advanced-search-prefix")),r=Array.from(document.querySelectorAll(".js-advanced-search-prefix:checked")),n=[...s(e),...s(t),...s(r)],c=n.reduce(((e,t)=>(t.value&&t.type&&e[t.type]++,e)),{Repositories:0,Users:0,Code:0,Issues:0}),a=n.reduce(((e,t)=>`${e} ${function({prefix:e,value:t}){return""===e?"":t?`${e}${t}`:""}(t)}`.trim()),""),u=document.querySelector(".js-advanced-search-input").value;document.querySelector(".js-type-value").value=function(e){let t=new URLSearchParams(window.location.search).get("type")||"Repositories",r=0;for(const n in e)e[n]>r&&(r=e[n],t=n);return t}(c),document.querySelector(".js-search-query").value=`${u} ${a}`.trim();const o=document.querySelector(".js-advanced-query");o.innerHTML="",o.textContent=a;const i=document.createElement("span");i.textContent=u.trim(),o.prepend(i," ")}function a(e){return-1!==e.search(/\s/g)?`"${e}"`:e}function s(e){return e.map((e=>{const t=e.value.trim(),r=e.getAttribute("data-search-prefix"),n=e.getAttribute("data-search-type");return""===r?{prefix:r,value:t,type:n}:-1!==t.search(/,/g)&&"location"!==r?t.split(/,/).map((e=>({prefix:r,value:a(e.trim()),type:n}))):{prefix:r,value:a(t),type:n}})).flatMap((e=>e))}e(".js-advanced-search-prefix",(function(){c()})),r("change",".js-advanced-search-prefix",c),t(".js-advanced-search-input",(function(e){const t=e.closest(".js-advanced-search-label");t.classList.add("focus"),e.addEventListener("blur",(()=>t.classList.remove("focus")),{once:!0})})),n(".js-advanced-search-input",(function(){c()}))}}}));
//# sourceMappingURL=chunk-advanced-f331d021.js.map
