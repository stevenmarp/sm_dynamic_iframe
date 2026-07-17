odoo.define("sm_dynamic_iframe.iframe_action", function (require) {
    "use strict";

    var AbstractAction = require("web.AbstractAction");
    var core = require("web.core");

    var SmIframeAction = AbstractAction.extend({
        template: "sm_dynamic_iframe.IframeAction",

        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.url = (action.params && action.params.url) || "about:blank";
        },
    });

    core.action_registry.add("sm_dynamic_iframe", SmIframeAction);

    return SmIframeAction;
});
