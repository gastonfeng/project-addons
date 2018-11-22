odoo.define('project_event.login_alert_message_saml', function (require) {
    "use strict";




function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

switch(getUrlVars()["saml_error"]){
    case "1":
        $("#password").after('<br/><p class="alert alert-danger" >Sign up is not allowed on this database.</p>');
        break;
    case "2":
        $("#password").after('<br/><p class="alert alert-danger" >Access Denied</p>');
        break;
    case "3":
        $("#password").after('<br/><p class="alert alert-danger" >You do not have access to this database or your invitation has expired. Please ask for an invitation and be sure to follow the link in your invitation email.</p>');
        break;
    default:
}

});
