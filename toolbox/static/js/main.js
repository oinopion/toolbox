// main

$(function() {
  $('.project[title]').twipsy();
  $('.date-picker').datepicker({
    beforeShowDay: $.datepicker.noWeekends,
    dateFormat: $.datepicker.ISO_8601,
    minDate: new Date(),
    showOtherMonths: true,
    selectOtherMonths: true,
    numberOfMonths: 2,
    firstDay: 1
  });

  $('.stories').sortable({
    handle: '.story-sort-handle',
    forcePlaceholderSize: true,
    placeholder: 'story row',
    update: function (ev, ui) {
      var item = ui.item;
      var next = item.next(), prev = item.prev();
      var form = $('#importance-form');
      form.find('#id_next_pk').val(next.data('pk'));
      form.find('#id_previous_pk').val(prev.data('pk'));
      form.attr('action', item.data('importance-update'));
      form.submit();
    }
  });
});

