(this["webpackJsonpdocassemble-app"]=this["webpackJsonpdocassemble-app"]||[]).push([[0],{105:function(e,t,a){},362:function(e,t,a){},363:function(e,t,a){"use strict";a.r(t);var n=a(1),s=a(0),r=a.n(s),i=a(18),o=a.n(i),c=(a(105),a(106),a(12)),d=a(8),l=a(9),u=a(11),p=a(10),h=a(14),b=a(24),j=a.n(b),O=a(74),m=a(99),f=a(13),v="WRITE_ANSWERS",g="SUBMIT_ANSWERS",x="GET_DATA",y="SET_SUBMITTED",q="SET_SEEN",w="GET_ERRORS",k="CREATE_MESSAGE",N="GET_CHECKIN",C="SET_HELP",_="SET_SOURCE",S=function(e,t,a){return{type:w,payload:{msg:e,status:t,variant:a}}},T=a(50),E=a.n(T),A=a(98),R=a(72),D={replace:function(e){if("style"===e.name){var t=document.createElement("style");return t.innerHTML=Object(R.renderToString)(Object(b.domToReact)(e.children,D)),document.head.appendChild(t),null}if("script"!==e.name)return null;var a=Object(R.renderToString)(Object(b.domToReact)(e.children,D));a&&(a=(a=(a=a.replace(/&quot;/g,'"')).replace(/&lt;/g,"<")).replace(/&gt;/g,">"),eval.call(window,a))}};function I(e){return"string"!==typeof e?null:j()(e,D)}function B(e,t){var a=e();if(a.data.question.script&&I(a.data.question.script),a.data.question.css&&a.data.question.questionName&&!a.seen[a.data.question.questionName]&&I(a.data.question.css),a.data.question.questionName){var n={};n[a.data.question.questionName]=!0,t({type:q,payload:n})}var s=a.data.location_bar.replace(/^https?:\/\/[^/]+/,"");null!=window.history.state&&a.data.question.steps>window.history.state.steps?window.history.pushState({steps:a.data.question.steps},s+" - page "+a.data.question.steps,s+a.data.page_sep+a.data.question.steps):window.history.replaceState({steps:a.data.question.steps},s+" - page "+a.data.question.steps,s+a.data.page_sep+a.data.question.steps)}var H=function(e){return{type:v,payload:{data:e}}},L=function(){return function(e,t){var a,n=t(),s={i:n.data.i||window.location.pathname+window.location.search,secret:n.data.secret||sessionStorage.getItem("daSecret")||"",user_code:n.data.user_code||sessionStorage.getItem("daUserCode")||""};n.data.session||(s.referer=document.referrer),E.a.get("http://localhost/api/interview?"+(a=s,Object.entries(a).map((function(e){return e.map(encodeURIComponent).join("=")})).join("&"))).then((function(a){if(a.data.redirect)window.location.href=a.data.redirect;else{"activeElement"in document&&document.activeElement.blur();var r={secret:n.data.secret||sessionStorage.getItem("daSecret"),user_code:n.data.user_code||sessionStorage.getItem("daUserCode")};a.data.secret&&s.secret!==a.data.secret&&sessionStorage.setItem("daSecret",a.data.secret),a.data.user_code&&s.user_code!==a.data.user_code&&sessionStorage.setItem("daUserCode",a.data.user_code),a.data.setup&&(a.data.setup.googleAnalytics.enabled&&A.a.initialize(a.data.setup.googleAnalytics.ga_id),a.data.setup.googleApiKey),e({type:x,payload:Object(c.a)(Object(c.a)({},r),a.data)});try{B(t,e)}catch(i){console.log(i)}}})).catch((function(t){console.log("got this fucking error1: "+t),e(S(t.response?t.response.data:t,t.response?t.response.status:0,"danger"))}))}};function F(e){return{type:y,payload:e}}var V=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).onClick=function(e){var t;try{t=JSON.parse(atob(e))}catch(a){return function(e){return console.log("Invalid action"),e.preventDefault(),!1}}return function(e){return this.props.callAction(t),e.preventDefault(),!1}}(e.actionData).bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"render",value:function(){return Object(n.jsx)("a",Object(c.a)(Object(c.a)({},this.props.otherProps),{},{href:"#action",onClick:this.onClick,children:this.props.contents}))}}]),a}(r.a.Component),M=Object(f.b)((function(e){return{data:e.data}}),{callAction:function(e){return function(t,a){var n=a(),s={i:n.data.i,secret:n.data.secret,user_code:n.data.user_code,command:"action",action:e};E.a.post("http://localhost/api/interview",s).then((function(e){"activeElement"in document&&document.activeElement.blur(),t({type:x,payload:e.data});try{B(a,t)}catch(n){console.log(n)}})).catch((function(e){console.log("got this fucking error4: "+e),t(S(e.response?e.response.data:"Error",e.response?e.response.status:0,"danger"))}))}}})(V),U=a(16),G=a(25),P=a(54),z=a(19);U.b.add(P.a,G.a);var Q=0;var W={replace:function(e){if(e.attribs){if("a"===e.name){if(e.attribs["data-js"])return Object(n.jsx)("a",{href:"#js",onClick:(e.attribs["data-js"],function(e){return e.preventDefault(),!1}),children:Object(b.domToReact)(e.children,W)});if(e.attribs["data-embaction"]){var t=Object(b.attributesToProps)(e.attribs);return Object(n.jsx)(M,{actionData:e.attribs["data-embaction"],otherProps:t,contents:Object(b.domToReact)(e.children,W)})}}if("i"===e.name&&e.attribs.class&&e.attribs.class.startsWith("fa")){var a=e.attribs.class.split(" ");return a[1]=a[1].replace(/^fa-/,""),Object(n.jsx)(z.a,{icon:a})}return"script"===e.name||"style"===e.name?null:"daterm"===e.attribs.class?Object(n.jsx)(m.a,{trigger:"click",transition:!1,placement:e.attribs["data-placement"]||"auto",overlay:(s=e.attribs,Object(n.jsx)(O.a,{id:"da_popover_"+Q++,children:Object(n.jsx)(O.a.Content,{children:j()(s["data-content"])})})),children:Object(n.jsx)("span",{className:"daterm",children:Object(b.domToReact)(e.children,W)})}):void 0;var s}}};function J(e){return"string"!==typeof e?null:j()(e,W)}var K=a(48),X=a(374),Y=a(373),Z=a(371);U.b.add(P.a,G.a);var $=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.data.phone?Object(n.jsx)(X.a.Item,{children:Object(n.jsxs)(X.a.Link,{role:"button",href:"#dahelp","data-target":"#dahelp",title:this.props.data.phone.title,className:"dapointer dahelptrigger",children:[Object(n.jsx)(z.a,{icon:["fas","phone"],className:"da-chat-active"}),Object(n.jsx)("span",{className:"sr-only",children:this.props.data.phone.label})]})}):null}}]),a}(r.a.Component),ee=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.data.chat?Object(n.jsx)(X.a.Item,{children:Object(n.jsxs)(X.a.Link,{href:"#dahelp","data-target":"#dahelp",className:"nav-link dapointer dahelptrigger",children:[Object(n.jsx)(z.a,{icon:["fas","comment-alt"]}),Object(n.jsx)("span",{className:"sr-only",children:this.props.data.chat.label})]})}):null}}]),a}(r.a.Component),te=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.data.question.help.specific&&!this.props.data.seenHelp?Object(n.jsxs)("span",{className:"daactivetext",children:[J(this.props.data.question.help.label)," ",Object(n.jsx)(z.a,{icon:["fas","star"]})]}):Object(n.jsx)(r.a.Fragment,{children:this.props.data.question.help.label})}}]),a}(r.a.Component),ae=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).doToggle=n.doToggle.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"doToggle",value:function(e){return e.preventDefault(),this.props.toggleHelp(),"activeElement"in document&&document.activeElement.blur(),!1}},{key:"render",value:function(){return this.props.data.question.help?Object(n.jsx)(X.a.Item,{children:Object(n.jsx)(X.a.Link,{className:"dapointer da-no-outline dahelptrigger",href:"#help",id:"dahelptoggle",onClick:this.doToggle,title:this.props.data.question.help.title,active:this.props.data.showHelp,children:Object(n.jsx)(te,{data:this.props.data})})}):null}}]),a}(r.a.Component),ne=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).doToggle=n.doToggle.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"doToggle",value:function(e){return e.preventDefault(),this.props.toggleSource(),"activeElement"in document&&document.activeElement.blur(),!1}},{key:"render",value:function(){return this.props.data.question.source?Object(n.jsx)(X.a.Item,{children:Object(n.jsx)(X.a.Link,{className:"da-no-outline d-none d-md-block",href:"#source",id:"dasourcetoggle",onClick:this.doToggle,title:this.props.data.question.source.title,active:this.props.data.showSource,children:this.props.data.question.source.label})}):null}}]),a}(r.a.Component),se=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).clickBackButton=n.clickBackButton.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"clickBackButton",value:function(e){return e.preventDefault(),this.props.goBack(),!1}},{key:"render",value:function(){return this.props.data.question.allow_going_back?Object(n.jsx)(Y.a.Brand,{href:"#",onClick:this.clickBackButton,children:Object(n.jsx)("button",{className:"dabackicon text-muted dabackbuttoncolor",title:this.props.data.question.backTitle,children:Object(n.jsxs)("span",{children:[Object(n.jsx)(z.a,{icon:["fas","chevron-left"]}),Object(n.jsx)("span",{className:"daback",children:this.props.data.question.cornerBackButton})]})})},"daback"):null}}]),a}(r.a.Component),re=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){if(!this.props.data.question.menu)return console.log("There is no menu."),null;if(0===this.props.data.question.menu.items.length)return Object(n.jsx)(X.a.Link,{href:this.props.data.question.menu.top.href||"#",children:this.props.data.question.menu.top.anchor});var e=this.props.data.question.menu.items.map((function(e){return Object(n.jsx)(Z.a.Item,{href:e.href,children:e.anchor})}));return Object(n.jsx)(Z.a,{title:this.props.data.question.menu.top.anchor,id:"basic-navbar-nav",children:e})}}]),a}(r.a.Component),ie=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.data&&this.props.data.question?Object(n.jsx)(Y.a,{bg:this.props.data.question.navbarVariant,variant:this.props.data.question.navbarVariant,expand:"md",className:"fixed-top",children:Object(n.jsxs)(K.a,{className:"danavcontainer justify-content-start",children:[Object(n.jsx)(se,{data:this.props.data,goBack:this.props.goBack}),Object(n.jsxs)(Y.a.Brand,{id:"dapagetitle",className:"danavbar-title dapointer",href:"#",children:[Object(n.jsx)("span",{className:"d-none d-md-block",children:J(this.props.data.question.title)}),Object(n.jsx)("span",{className:"d-block d-md-none",children:J(this.props.data.question.short_title)})]},"datitle"),Object(n.jsxs)(X.a,{className:"damynavbar-right",children:[Object(n.jsx)(ne,{data:this.props.data,toggleSource:this.props.toggleSource}),Object(n.jsx)(ae,{data:this.props.data,toggleHelp:this.props.toggleHelp}),Object(n.jsx)($,{data:this.props.data}),Object(n.jsx)(ee,{data:this.props.data})]}),Object(n.jsx)(Y.a.Toggle,{"aria-controls":"basic-navbar-nav",className:"ml-auto"}),Object(n.jsx)(Y.a.Collapse,{id:"basic-navbar-nav",children:Object(n.jsx)(X.a,{className:"ml-auto",children:Object(n.jsx)(re,{data:this.props.data})})})]})}):null}}]),a}(r.a.Component),oe=Object(f.b)((function(e){return{submitted:e.submitted,answers:e.answers,data:e.data}}),{goBack:function(){return function(e,t){var a=t(),n={i:a.data.i,secret:a.data.secret,user_code:a.data.user_code,command:"back"};E.a.post("http://localhost/api/interview",n).then((function(a){"activeElement"in document&&document.activeElement.blur(),e({type:x,payload:a.data});try{B(t,e)}catch(n){console.log(n)}})).catch((function(t){console.log("got this fucking error2: "+t),e(S(t.response?t.response.data:"Error",t.response?t.response.status:0,"danger"))}))}},toggleHelp:function(){return function(e,t){var a=t();e({type:C,payload:{showHelp:!a.data.showHelp,seenHelp:!0}})}},toggleSource:function(){return function(e,t){var a=t();e({type:_,payload:{showSource:!a.data.showSource}})}}})(ie),ce=a(45),de=a(23),le=a(21),ue=a(28),pe=a(33);U.b.add(G.a);var he=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.decoration?this.props.decoration.url?Object(n.jsx)("img",{className:"daiconfloat",alt:"",src:this.props.decoration.url,style:{width:this.props.decoration.size.width,height:this.props.decoration.size.height}}):this.props.decoration.name?Object(n.jsx)("span",{style:{"font-size":this.props.decoration.size},children:Object(n.jsx)(z.a,{icon:["fas",this.props.decoration.name]})}):null:null}}]),a}(r.a.Component),be=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.html?Object(n.jsxs)("div",{className:"da-page-header",children:[Object(n.jsxs)("h1",{className:"h3",id:"daMainQuestion",children:[Object(n.jsx)(he,{decoration:this.props.decoration}),J(this.props.html)]}),Object(n.jsx)("div",{className:"daclear"})]}):null}}]),a}(r.a.Component),je=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.html?Object(n.jsx)("div",{className:"da-subquestion",children:J(this.props.html)}):null}}]),a}(r.a.Component),Oe=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).onChangeValue=n.onChangeValue.bind(Object(h.a)(n)),n.onChangeRadio=n.onChangeRadio.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"onChangeValue",value:function(e){this.props.writeAnswers(Object(le.a)({},this.props.name,e.target.value))}},{key:"onChangeRadio",value:function(e){}},{key:"render",value:function(){var e=this,t=0;return Object(n.jsx)("fieldset",{className:"da-field-radio",children:Object(n.jsx)("div",{className:"mb-3",onChange:this.onChangeValue,children:this.props.choices.map((function(a){return Object(n.jsx)(ue.a.Check,{type:"radio",value:a.value,label:J(a.label),name:e.props.fieldName,id:e.props.fieldName+"_"+t++,onChange:e.onChangeRadio,checked:e.props.answers[e.props.name]===a.value},e.props.fieldName+"_"+t)}))})})}}]),a}(r.a.Component),me=Object(f.b)((function(e){return{answers:e.answers}}),{writeAnswers:H})(Oe);function fe(e){return!(!e||"False"===e||"false"===e)}function ve(e){var t="da-field-container";return e.required&&(t+=" darequired"),"text"===e.datatype&&(t+=" da-field-container-datatype-text"),"html"!==e.datatype&&"note"!==e.datatype||(t+=" row da-field-container-note"),t}var ge=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).handleChange=n.handleChange.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"handleChange",value:function(e){this.props.writeAnswers(Object(le.a)({},this.props.data.question.fields[this.props.indexNo].variable_name,e.target.value))}},{key:"render",value:function(){var e,t=this.props.data.question.fields[this.props.indexNo];return t.label?Object(n.jsxs)(ue.a.Group,{as:this.props.as,controlId:"field"+this.props.indexNo,className:ve(t),children:[Object(n.jsx)(ue.a.Label,{children:J(t.label)}),Object(n.jsx)(ue.a.Control,{type:(e=t.datatype,"date"===e?"date":"text"),placeholder:t.hint?J(t.hint):null,onChange:this.handleChange,value:this.props.answers[t.variable_name]?this.props.answers[t.variable_name]:""})]},"field"+this.props.indexNo):"html"===t.datatype?Object(n.jsx)(ue.a.Group,{as:this.props.as,controlId:"field"+this.props.indexNo,className:ve(t),children:Object(n.jsx)(de.a,{md:12,children:Object(n.jsx)("div",{children:J(t.html)})})},"field"+this.props.indexNo):void 0}}]),a}(r.a.Component),xe=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e=this,t=this.props.data.question.fields[this.props.indexNo];if(!t.active)return null;if(this.props.indexNo>0&&fe(this.props.data.question.fields[this.props.indexNo-1].inline)&&fe(t.inline))return null;if(t.inline){for(var a=this.props.data.question.fields.length,s=[],r=this.props.indexNo;r<a&&this.props.data.question.fields[r].inline;++r)s.push(r);return Object(n.jsx)(ue.a.Row,{children:s.map((function(t){return Object(n.jsx)(ge,{indexNo:t,as:de.a,data:e.props.data,writeAnswers:e.props.writeAnswers,answers:e.props.answers},"individualfieldgroup"+t)}))},"individualfield"+this.props.indexNo)}return Object(n.jsx)(ge,{indexNo:this.props.indexNo,data:this.props.data,writeAnswers:this.props.writeAnswers,answers:this.props.answers})}}]),a}(r.a.Component),ye=Object(f.b)((function(e){return{submitted:e.submitted,answers:e.answers,data:e.data}}),{writeAnswers:H})(xe),qe=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e=this;if("multiple_choice"===this.props.data.question.questionType)return"radio"===this.props.data.question.questionVariety?Object(n.jsx)(me,{name:this.props.data.question.fields[0].variable_name,fieldName:"_field_0",choices:this.props.data.question.fields[0].choices,answers:this.props.answers}):null;if("fields"===this.props.data.question.questionType){var t=0;return Object(n.jsx)(r.a.Fragment,{children:this.props.data.question.fields.map((function(a){return Object(n.jsx)(ye,{indexNo:t++,data:e.props.data},"indivfield"+t)}))})}return null}}]),a}(r.a.Component),we=Object(f.b)((function(e){return{submitted:e.submitted,answers:e.answers,data:e.data}}))(qe),ke=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).onClick=function(e){this.props.writeAnswers(Object(le.a)({},this.props.data.question.fields[0].variable_name,this.props.value))}.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"render",value:function(){return Object(n.jsx)(pe.a,{variant:this.props.variant||"primary",className:"btn-da",type:"submit",onClick:this.onClick,disabled:!!this.props.submitted,children:J(this.props.inner)})}}]),a}(r.a.Component),Ne=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e=this;if("multiple_choice"===this.props.data.question.questionType){if("radio"===this.props.data.question.questionVariety)return Object(n.jsx)("fieldset",{className:"da-field-buttons",children:Object(n.jsx)("div",{children:Object(n.jsx)(pe.a,{variant:"primary",className:"btn-da",type:"submit",disabled:!!this.props.submitted,children:this.props.data.question.continueLabel},"button_0")})});if("buttons"===this.props.data.question.questionVariety){var t=0;return Object(n.jsx)("fieldset",{className:"da-field-buttons",children:Object(n.jsx)("div",{children:this.props.data.question.fields[0].choices.map((function(a){return Object(n.jsxs)(r.a.Fragment,{children:[Object(n.jsx)(ke,{variant:"primary",data:e.props.data,submitted:!!e.props.submitted,writeAnswers:e.props.writeAnswers,value:a.value,inner:a.label},"button"+t)," "]},"buttonfragment"+t++)}))})})}return null}return"yesno"===this.props.data.question.questionType?(console.log("I am in the yesno"),Object(n.jsx)("fieldset",{className:"da-field-yesno",children:Object(n.jsxs)("div",{children:[Object(n.jsx)(ke,{variant:"primary",value:!0,data:this.props.data,writeAnswers:this.props.writeAnswers,submitted:!!this.props.submitted,inner:this.props.data.question.yesLabel},"button_0")," ",Object(n.jsx)(ke,{variant:"secondary",data:this.props.data,writeAnswers:this.props.writeAnswers,value:!1,submitted:!!this.props.submitted,inner:this.props.data.question.noLabel},"button_1")]})})):"fields"===this.props.data.question.questionType||"settrue"===this.props.data.question.questionType?Object(n.jsx)("fieldset",{className:"da-field-buttons",children:Object(n.jsx)("div",{className:"form-actions",children:Object(n.jsx)(pe.a,{variant:"primary",className:"btn-da",type:"submit",disabled:!!this.props.submitted,children:this.props.data.question.continueLabel},"button_0")})}):null}}]),a}(r.a.Component),Ce=Object(f.b)((function(e){return{submitted:e.submitted,answers:e.answers,data:e.data}}),{writeAnswers:H})(Ne);U.b.add(G.a);var _e=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(d.a)(this,a),(n=t.call(this)).onSubmit=function(e){e.preventDefault(),"settrue"===n.props.data.question.questionType?n.props.writeAnswers(Object(le.a)({},n.props.data.question.fields[0].variable_name,!0)):n.props.data.question.question_variable_name&&n.props.writeAnswers(Object(le.a)({},n.props.data.question.question_variable_name,!0)),n.props.setSubmitted(!0),n.props.submitData()},n.backToQuestion=n.backToQuestion.bind(Object(h.a)(n)),n}return Object(l.a)(a,[{key:"backToQuestion",value:function(e){return e.preventDefault(),this.props.setHelp(!1),!1}},{key:"render",value:function(){if(!this.props.data.question||!this.props.data.question.questionText)return Object(n.jsx)("div",{className:"daSpinnerDiv",children:Object(n.jsx)(z.a,{icon:"spinner",spin:!0})});if(this.props.data.showHelp&&this.props.data.question.help){return Object(n.jsxs)(r.a.Fragment,{children:[Object(n.jsx)("div",{className:"mt-2 mb-2",children:Object(n.jsxs)(pe.a,{variant:"info",onClick:this.backToQuestion,children:[Object(n.jsx)(z.a,{icon:["fas","caret-left"]})," ",this.props.data.question.helpBackLabel]})}),this.props.data.question.helpText.map((function(e){return Object(n.jsxs)(r.a.Fragment,{children:[e.heading?Object(n.jsx)("div",{className:"da-page-header",children:Object(n.jsx)("h1",{className:"h3",children:J(e.heading)})}):null,Object(n.jsx)("div",{children:J(e.content)})]},"help0")}))]})}return Object(n.jsxs)(ue.a,{onSubmit:this.onSubmit,children:[Object(n.jsx)(be,{html:this.props.data.question.questionText,decoration:this.props.data.question.decoration}),Object(n.jsx)(je,{html:this.props.data.question.subquestionText}),Object(n.jsx)(we,{}),Object(n.jsx)(Ce,{})]})}}]),a}(r.a.Component),Se=Object(f.b)((function(e){return{submitted:e.submitted,answers:e.answers,data:e.data}}),{writeAnswers:H,submitAnswers:function(e){return{type:g,payload:{data:e}}},getData:L,setSubmitted:F,submitData:function(){return function(e,t){var a=t(),n={i:a.data.i,secret:a.data.secret,user_code:a.data.user_code,variables:a.answers};E.a.post("http://localhost/api/interview",n).then((function(a){"activeElement"in document&&document.activeElement.blur(),e({type:x,payload:a.data});try{B(t,e)}catch(n){console.log(n)}})).catch((function(t){console.log("got this fucking error3: "+t),e(S(t.response?t.response.data:"Error",t.response?t.response.status:0,"danger"))}))}},setHelp:function(e){return{type:C,payload:{showHelp:e}}}})(_e),Te=a(95),Ee=a(372),Ae=a(73),Re=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.item.code?Object(n.jsx)(Ee.a,{language:"yaml",style:Ae.a,children:this.props.item.code}):null}}]),a}(r.a.Component),De=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){return this.props.item.source_file?Object(n.jsx)("p",{children:Object(n.jsx)("small",{children:Object(n.jsxs)("strong",{children:["(from ",this.props.item.source_file,")"]})})}):null}}]),a}(r.a.Component),Ie=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){switch(this.props.item.reason){case"needed":return Object(n.jsxs)("h5",{children:[this.props.item.reason_text+" ",Object(n.jsx)("code",{children:this.props.item.variable_name})," at"," ",this.props.item.time]});default:return Object(n.jsxs)("h5",{children:[this.props.item.reason_text," at ",this.props.item.time]})}}}]),a}(r.a.Component),Be=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"render",value:function(){var e;return this.props.data.showSource&&this.props.data.question.source?(e=this.props.data.showHelp?"help":"question",Object(n.jsxs)(r.a.Fragment,{children:[Object(n.jsx)(ce.a,{children:Object(n.jsxs)(de.a,{xl:6,lg:6,md:8,sm:12,className:"offset-xl-3 offset-lg-3 offset-md-2",children:[Object(n.jsx)("h3",{children:"Readability"}),Object(n.jsxs)(Te.a,{children:[Object(n.jsx)("thead",{children:Object(n.jsxs)("tr",{children:[Object(n.jsx)("th",{children:"Formula"}),Object(n.jsx)("th",{children:"Score"})]})}),Object(n.jsx)("tbody",{children:this.props.data.question.source.readability[e].map((function(e){return Object(n.jsxs)("tr",{children:[Object(n.jsx)("td",{children:e[0]}),Object(n.jsx)("td",{children:e[1]})]},e[0])}))})]})]})}),Object(n.jsx)(ce.a,{children:Object(n.jsxs)(de.a,{md:12,children:[Object(n.jsx)("a",{rel:"noreferrer",target:"_blank",href:this.props.data.question.source.varsLink,children:this.props.data.question.source.varsLabel}),Object(n.jsx)("h3",{children:"Source code for question"}),Object(n.jsx)(Ee.a,{language:"yaml",style:Ae.a,children:this.props.data.question.source.history.source_code}),Object(n.jsx)("h4",{children:"How question came to be asked"}),Object(n.jsx)(r.a.Fragment,{children:this.props.data.question.source.history.steps.map((function(e){return Object(n.jsxs)(r.a.Fragment,{children:[Object(n.jsx)(Ie,{item:e}),Object(n.jsx)(De,{item:e}),Object(n.jsx)(Re,{item:e})]},"Step_"+e.index)}))})]})})]})):null}}]),a}(r.a.Component),He=Object(f.b)((function(e){return{data:e.data}}))(Be),Le=a(63),Fe=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"componentDidUpdate",value:function(e){var t=this.props,a=t.error,n=t.alert;a!==e.error&&(console.log("msg is "+a.msg),a.msg&&(console.log("Doing alert"),n.error("".concat(a.msg))))}},{key:"render",value:function(){return Object(n.jsx)(s.Fragment,{})}}]),a}(s.Component),Ve=Object(f.b)((function(e){return{error:e.errors,message:e.messages}}))(Object(Le.b)()(Fe));U.b.add(G.a);var Me=function(e){Object(u.a)(a,e);var t=Object(p.a)(a);function a(){return Object(d.a)(this,a),t.apply(this,arguments)}return Object(l.a)(a,[{key:"componentDidMount",value:function(){this.props.getData(),this.props.setSubmitted(!1)}},{key:"render",value:function(){return this.props.data.question&&this.props.data.question.questionText?Object(n.jsxs)("div",{className:"da-pad-for-navbar",children:[Object(n.jsx)(oe,{}),Object(n.jsxs)(K.a,{id:"mainContainer",children:[Object(n.jsx)(ce.a,{children:Object(n.jsxs)(de.a,{xl:6,lg:6,md:8,className:"offset-xl-3 offset-lg-3 offset-md-2",children:[Object(n.jsx)(Se,{}),Object(n.jsxs)("div",{children:["Here are the answers: ",JSON.stringify(this.props.answers)]}),Object(n.jsx)(Ve,{})]})}),Object(n.jsx)(He,{})]})]}):Object(n.jsx)(K.a,{className:"h-100",children:Object(n.jsx)(ce.a,{className:"h-100 justify-content-center align-items-center",children:Object(n.jsx)(de.a,{xs:12,className:"text-center dahuge",children:Object(n.jsx)(z.a,{icon:"spinner",spin:!0})})})})}}]),a}(r.a.Component),Ue=Object(f.b)((function(e){return{seen:e.seen,answers:e.answers,data:e.data}}),{getData:L,setSubmitted:F})(Me),Ge=(a(362),a(31)),Pe=a(96),ze=a(97),Qe={};var We=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:Qe,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case v:return Object(c.a)(Object(c.a)({},e),t.payload.data);case g:return Object(c.a)(Object(c.a)({},e),t.payload);case x:var a={};if(t.payload.question.fields)for(var n=t.payload.question.fields.length,s=0;s<n;++s)t.payload.question.fields[s].variable_name&&void 0!==t.payload.question.fields[s].default&&null!==t.payload.question.fields[s].default&&(a[t.payload.question.fields[s].variable_name]=t.payload.question.fields[s].default);return a;default:return e}},Je={};var Ke=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:Je,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case x:return Object(c.a)(Object(c.a)({},e),{},{question:{},seenHelp:null,showHelp:null},t.payload);case N:case C:case _:return Object(c.a)(Object(c.a)({},e),t.payload);default:return e}};var Xe=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:null,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case y:return!!t.payload;case x:return!1;default:return e}},Ye={msg:{},status:null,variant:"danger"};var Ze=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:Ye,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case w:return console.log("reducing GET_ERRORS"),{msg:t.payload.msg,status:t.payload.status,variant:t.payload.variant};default:return e}},$e={};var et=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:$e,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case k:return t.payload;default:return e}},tt={};var at=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:tt,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case q:return Object(c.a)(Object(c.a)({},e),t.payload);default:return e}},nt=Object(Ge.combineReducers)({data:Ke,answers:We,submitted:Xe,errors:Ze,messages:et,seen:at}),st=[ze.a],rt=Object(Ge.createStore)(nt,{data:{question:{}}},Object(Pe.composeWithDevTools)(Ge.applyMiddleware.apply(void 0,st))),it={timeout:5e3,position:"top center",containerStyle:{marginTop:"60px"}},ot=function(e){var t=e.style,a=(e.options,e.message),s=e.close;return Object(n.jsxs)("div",{className:"alert alert-danger ",role:"alert",style:t,children:[a,Object(n.jsx)("button",{onClick:s,type:"button",className:"close",children:Object(n.jsx)("span",{"aria-hidden":"true",children:"\xd7"})})]})};var ct=function(){return Object(n.jsx)(f.a,{store:rt,children:Object(n.jsx)(Le.a,Object(c.a)(Object(c.a)({template:ot},it),{},{children:Object(n.jsx)(Ue,{})}))})},dt=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,375)).then((function(t){var a=t.getCLS,n=t.getFID,s=t.getFCP,r=t.getLCP,i=t.getTTFB;a(e),n(e),s(e),r(e),i(e)}))};o.a.render(Object(n.jsx)(r.a.StrictMode,{children:Object(n.jsx)(ct,{})}),document.getElementById("root")),dt()}},[[363,1,2]]]);
//# sourceMappingURL=main.9712d22f.chunk.js.map