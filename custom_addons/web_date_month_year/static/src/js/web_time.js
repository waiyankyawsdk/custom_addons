
odoo.define('web_date_month_year.time', function(require){
    var time = require('web.time');
    var core = require('web.core');
    var _t = core._t;

    /**
     * Get month format of the user's language
     */
    time.getLangMonthFormat = function getLangMonthFormat() {
        return time.strftime_to_moment_format(_t.database.parameters.month_format);
    }
    /**
     * Get year format of the user's language
     */
    time.getLangYearFormat = function getLangYearFormat() {
        return time.strftime_to_moment_format(_t.database.parameters.year_format);
    }

    return time;
})

