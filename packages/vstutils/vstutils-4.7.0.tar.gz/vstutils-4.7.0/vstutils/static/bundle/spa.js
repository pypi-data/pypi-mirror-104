window.spa=function(e){function t(t){for(var o,r,a=t[0],l=t[1],c=t[2],u=0,g=[];u<a.length;u++)r=a[u],Object.prototype.hasOwnProperty.call(s,r)&&s[r]&&g.push(s[r][0]),s[r]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);for(f&&f(t);g.length;)g.shift()();return i.push.apply(i,c||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],o=!0,a=1;a<n.length;a++){var l=n[a];0!==s[l]&&(o=!1)}o&&(i.splice(t--,1),e=r(r.s=n[0]))}return e}var o={},s={5:0},i=[];function r(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,r),n.l=!0,n.exports}r.m=e,r.c=o,r.d=function(e,t,n){r.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},r.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},r.t=function(e,t){if(1&t&&(e=r(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(r.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)r.d(n,o,function(t){return e[t]}.bind(null,o));return n},r.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return r.d(t,"a",t),t},r.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},r.p="/static/bundle/";var a=window.webpackJsonp_name_=window.webpackJsonp_name_||[],l=a.push.bind(a);a.push=t,a=a.slice();for(var c=0;c<a.length;c++)t(a[c]);var f=l;return i.push([286,0,2,4,1]),n()}({274:function(e,t,n){var o=n(5),s=n(275);"string"==typeof(s=s.__esModule?s.default:s)&&(s=[[e.i,s,""]]);var i={insert:"head",singleton:!1};o(s,i);e.exports=s.locals||{}},275:function(e,t,n){(t=n(6)(!1)).push([e.i,".ansi-black-fg{color:#000000}.ansi-red-fg{color:#ff6060}.ansi-green-fg{color:#60ff60}.ansi-yellow-fg{color:#ffff36}.ansi-blue-fg{color:#6060ff}.ansi-magenta-fg{color:#ff36ff}.ansi-cyan-fg{color:#36ffff}.ansi-white-fg{color:#ececec}.ansi-bright-black-fg{color:#363636}.ansi-bright-red-fg{color:#ff8080}.ansi-bright-green-fg{color:#80ff80}.ansi-bright-yellow-fg{color:#ffff80}.ansi-bright-blue-fg{color:#8080ff}.ansi-bright-magenta-fg{color:#ff80ff}.ansi-bright-cyan-fg{color:#80ffff}.ansi-bright-white-fg{color:#ffffff}.ansi-black-bg{background-color:#000000}.ansi-red-bg{background-color:#ff6060}.ansi-green-bg{background-color:#60ff60}.ansi-yellow-bg{background-color:#ffff36}.ansi-blue-bg{background-color:#6060ff}.ansi-magenta-bg{background-color:#ff36ff}.ansi-cyan-bg{background-color:#36ffff}.ansi-white-bg{background-color:#ececec}.ansi-bright-black-bg{background-color:#363636}.ansi-bright-red-bg{background-color:#ff8080}.ansi-bright-green-bg{background-color:#80ff80}.ansi-bright-yellow-bg{background-color:#ffff80}.ansi-bright-blue-bg{background-color:#8080ff}.ansi-bright-magenta-bg{background-color:#ff80ff}.ansi-bright-cyan-bg{background-color:#80ffff}.ansi-bright-white-bg{background-color:#ffffff}\n",""]),e.exports=t},286:function(e,t,n){"use strict";n.r(t),n.d(t,"TabSignal",(function(){return v.a})),n.d(t,"signals",(function(){return y.a})),n.d(t,"colors",(function(){return o})),n.d(t,"ComponentsRegistrator",(function(){return c.a})),n.d(t,"globalComponentsRegistrator",(function(){return c.b})),n.d(t,"AppRoot",(function(){return g.a})),n.d(t,"utils",(function(){return u})),n.d(t,"guiCustomizer",(function(){return B})),n.d(t,"setupVue",(function(){return q})),n.d(t,"popUp",(function(){return f})),n.d(t,"fields",(function(){return D})),n.d(t,"components",(function(){return E})),n.d(t,"models",(function(){return b})),n.d(t,"querySet",(function(){return m})),n.d(t,"views",(function(){return d})),n.d(t,"store",(function(){return h})),n.d(t,"router",(function(){return w})),n.d(t,"api",(function(){return l})),n.d(t,"users",(function(){return Q})),n.d(t,"dashboard",(function(){return N})),n.d(t,"BaseWidget",(function(){return N.BaseWidget})),n.d(t,"CounterWidget",(function(){return N.CounterWidget})),n.d(t,"CardWidget",(function(){return N.CardWidget})),n.d(t,"App",(function(){return $}));var o={};n.r(o),n.d(o,"AnsiUp",(function(){return I.a})),n.d(o,"ansiToHTML",(function(){return W}));var s=n(9),i=n(60),r=n(137),a=n.n(r),l=n(11),c=n(8),f=n(4),u=n(0),g=n(55),p=n(139);var d=n(33),h=n(23),b=n(27),w=n(54),m=n(32),C=n(62),v=n.n(C),y=n(7),k=(n(14),n(248),n(249),n(251),n(253),n(132),n(13)),_=n.n(k),R=(n(257),n(79)),M=n.n(R),S=n(77),T=n.n(S),x=n(21),j=n.n(x),O=(n(258),n(57)),L=n.n(O),A=(n(260),n(78)),P=n.n(A),V=(n(84),n(85),n(86)),I=n.n(V);n(274);const F=new I.a;function W(e){return F.ansi_to_html(e).replace(/\t/g,"&nbsp;&nbsp;&nbsp;&nbsp;")}F.use_classes=!0;var B=n(76),q=n(133),D=n(19),E=n(136),Q=n(66),N=n(61);n(135);window.SELECT2_THEME="bootstrap",n(254),n(255),window.moment=_.a,window.md5=M.a,window.Visibility=T.a,window.IMask=j.a,window.iziToast=L.a,window.autoComplete=P.a;const U=(e,t)=>{if(0===e)return 0;const n=e>10&&e<20,o=e%10==1;return t<4?!n&&o?1:2:!n&&o?1:!n&&e%10>=2&&e%10<=4||t<4?2:3};class $ extends class{constructor(e,t){this.config=e,this.schema=e.schema,this.router=null,this.cache=t,this.api=l.apiConnector.initConfiguration(e),this.translationsManager=new p.a(l.apiConnector,t),this.centrifugoClient=function(e,t){if(!e)return null;const n=new a.a(new URL("connection/websocket",e).toString());return t&&n.setToken(t),n}(this.schema.info["x-centrifugo-address"],this.schema.info["x-centrifugo-token"]),this.error_handler=new f.ErrorHandler,this.languages=null,this.translations=null,this.user=null,this.global_components=c.b,this.appRootComponent=g.a,this.initLanguage=u.guiLocalSettings.get("lang")||Object(u.getCookie)("lang")||"en"}afterInitialDataBeforeMount(){}async start(){this.centrifugoClient&&this.centrifugoClient.connect();const[e,t,n]=await Promise.all([this.translationsManager.getLanguages(),this.translationsManager.getTranslations(this.initLanguage),this.api.loadUser()]);this.languages=e,this.translations={[this.initLanguage]:t},this.user=n,this.afterInitialDataBeforeMount(),this.global_components.registerAll(),this.prepare()}changeAppRootComponent(e){this.appRootComponent=e}resetAppRootComponent(){this.appRootComponent=g.a}prepare(){}}{constructor(e,t,n,o){super(e,t),this.fieldsClasses=n,this.modelsClasses=o,this.views=null,this.modelsResolver=null,this.qsResolver=null,this.application=null}afterInitialDataBeforeMount(){this.prepareFieldsClasses(),new b.ModelConstructor(l.openapi_dictionary,this.config.schema,this.fieldsClasses,this.modelsClasses).generateModels(),this.modelsResolver=new b.ModelsResolver(this.modelsClasses,this.fieldsClasses,this.config.schema),this.views=new d.ViewConstructor(l.openapi_dictionary,this.modelsClasses,this.fieldsClasses).generateViews(this.config.schema),this.qsResolver=new m.QuerySetsResolver(this.modelsClasses,this.views),this.setNestedViewsQuerysets(),this.prepareViewsModelsFields()}prepareFieldsClasses(){for(const e of this.fieldsClasses.values())e.app=this}prepareViewsModelsFields(){for(const[e,t]of this.views)if(t.objects)for(const n of new Set(Object.values(t.objects.models)))for(const t of n.fields.values())t.prepareFieldForView(e)}setNestedViewsQuerysets(){for(const e of this.views.values())if(e instanceof d.PageNewView&&e.nestedAllowAppend){const t=e.listView,n=t.objects.getModelClass(u.RequestTypes.LIST).name;try{t.nestedQueryset=this.qsResolver.findQuerySetForNested(n,t.path)}catch(n){console.warn(n),e.nestedAllowAppend=!1,t.actions.delete("add")}}}setLanguage(e){return this._prefetchTranslation(e).then(e=>(this.application.$i18n.locale=e,u.guiLocalSettings.set("lang",e),window.spa.signals.emit("app.language.changed",{lang:e}),e))}_prefetchTranslation(e){return Object.values(this.languages).map(e=>e.code).includes(e)?this.translations[e]?Promise.resolve(e):this.translationsManager.getTranslations(e).then(t=>(this.translations={...this.translations,[e]:t},this.application.$i18n.setLocaleMessage(e,t),e)).catch(e=>{throw e}):Promise.reject(!1)}prepare(){y.a.emit("app.beforeInit",{app:this});let e=new h.StoreConstructor(this.views,this.config.isDebug);y.a.emit("app.beforeInitStore",{storeConstructor:e});let t=new w.RouterConstructor(this.views,w.mixins.routesComponentsTemplates,w.mixins.customRoutesComponentsTemplates);y.a.emit("app.beforeInitRouter",{routerConstructor:t}),this.router=t.getRouter();let n=new i.a({locale:this.initLanguage,messages:this.translations,silentTranslationWarn:!0,pluralizationRules:{ru:U}});s.a.prototype.$app=this,this.application=new s.a({mixins:[this.appRootComponent],propsData:{info:this.config.schema.info,x_menu:this.config.schema.info["x-menu"],x_docs:this.config.schema.info["x-docs"],a_links:!1},router:this.router,store:e.getStore(),i18n:n}),y.a.emit("app.afterInit",{app:this})}mount(){this.application.$mount("#RealBody")}}window.App=$}});