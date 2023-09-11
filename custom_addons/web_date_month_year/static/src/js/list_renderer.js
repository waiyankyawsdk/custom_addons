odoo.define('web_date_month_year.list_renderer', function (require) {
"use strict";

var ListRenderer = require('web.ListRenderer');
var pyUtils = require('web.py_utils')

ListRenderer.include({
    /**
     * Render a cell for the table. For most cells, we only want to display the
     * formatted value, with some appropriate css class. However, when the
     * node was explicitely defined with a 'widget' attribute, then we
     * instantiate the corresponding widget.
     *
     * @private
     * @param {Object} record
     * @param {Object} node
     * @param {integer} colIndex
     * @param {Object} [options]
     * @param {Object} [options.mode]
     * @param {Object} [options.renderInvisible=false]
     *        force the rendering of invisible cell content
     * @param {Object} [options.renderWidgets=false]
     *        force the rendering of the cell value thanks to a widget
     * @returns {jQueryElement} a <td> element
     */
    _renderBodyCell: function (record, node, colIndex, options) {

        // customize here, attach options to format month/year date
        if (node.attrs.options) {
            var name = node.attrs.name;
            var field = this.state.fields[name];
            var new_options = !_.isEmpty(node.attrs.options) && _.isString(node.attrs.options) && pyUtils.py_eval(node.attrs.options) || {};
            if (field) {
                field.options = new_options.datepicker && new_options || {}
            };
        }
        return this._super.call(this, record, node, colIndex, options);
    }
})
})