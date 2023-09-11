odoo.define('web_date_month_year.fields_utils', function (require) {
    "use strict";

    var core = require('web.core');
    var field_utils = require('web.field_utils');
    var time = require('web.time');
    var session = require('web.session');

    var _t = core._t;


    function formatDate(value, field, options) {
        if (value === false || isNaN(value)) {
            return "";
        }
        if (field && field.type === 'datetime') {
            if (!options || !('timezone' in options) || options.timezone) {
                value = value.clone().add(session.getTZOffset(value), 'minutes');
            }
        }
        var date_format = time.getLangDateFormat();

        // start - customize here
        if (field && field.options) {
            options = _.defaults(options || {}, field.options)
        }
        if (options && options.datepicker && (options.datepicker.showType == 'months' || options.datepicker.showType == 'years')) {
            date_format = options.datepicker.showType == 'months' ?
                time.getLangMonthFormat() :
                time.getLangYearFormat()
        }
        // end - customize here

        return value.format(date_format);
    };

    function parseDate(value, field, options) {
        if (!value) {
            return false;
        }
        var datePattern = time.getLangDateFormat();

        // start - customize here
        if (field && field.options) {
            options = _.defaults(options || {}, field.options)
        }
        if (options && options.datepicker && (options.datepicker.showType == 'months' || options.datepicker.showType == 'years')) {
            var datePattern = options.datepicker.showType == 'months' ?
                time.getLangMonthFormat() :
                time.getLangYearFormat()
        }
        // end- customize here

        var datePatternWoZero = datePattern.replace('MM', 'M').replace('DD', 'D');
        var date;
        if (options && options.isUTC) {
            date = moment.utc(value);
        } else {
            date = moment.utc(value, [datePattern, datePatternWoZero, moment.ISO_8601]);
        }
        if (date.isValid()) {
            if (date.year() === 0) {
                date.year(moment.utc().year());
            }
            if (date.year() >= 1900) {
                date.toJSON = function () {
                    return this.clone().locale('en').format('YYYY-MM-DD');
                };
                return date;
            }
        }
        throw new Error(_.str.sprintf(core._t("'%s' is not a correct date"), value));
    }
    // override methods
    field_utils.format.date = formatDate;
    field_utils.parse.date = parseDate;
})
