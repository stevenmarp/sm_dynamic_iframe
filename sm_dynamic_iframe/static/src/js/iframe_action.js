/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

export class SmIframeAction extends Component {
    static template = "sm_dynamic_iframe.IframeAction";
    static props = { "*": true };

    get url() {
        return (this.props.action.params && this.props.action.params.url) || "about:blank";
    }
}

registry.category("actions").add("sm_dynamic_iframe", SmIframeAction);
