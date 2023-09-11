odoo.define('web_date_month_year.datepicker', function (require) {
"use strict";

var core = require('web.core');
var DatePicker = require('web.datepicker');
var field_utils = require('web.field_utils');
var time = require('web.time');

DatePicker.DateWidget.include({
        init: function (parent, options) {
            this._super.apply(this, arguments);
            var _options = {};
            if (options && (options.showType==="months" || options.showType==="years")) {
                _options.showType = options.showType;
                _options.format = (options.showType === "months")
                                    ? time.getLangMonthFormat()
                                    : time.getLangYearFormat()
            }
            this.options = _.defaults(_options || {}, this.options)
        },
        /**
         * @private
         * @param {Moment} v
         * @returns {string}
         */
        _formatClient: function (v) {
            return field_utils.format[this.type_of_date](v, null, {
                timezone: false,
                datepicker: {
                    showType: this.options.showType,
                }
            });
        },
        /**
         * @private
         * @param {string|false} v
         * @returns {Moment}
         */
        _parseClient: function (v) {
            return field_utils.parse[this.type_of_date](v, null, {
                timezone: false,
                datepicker: {
                    showType: this.options.showType,
                }
            });
        },

    });
return DatePicker;
})

