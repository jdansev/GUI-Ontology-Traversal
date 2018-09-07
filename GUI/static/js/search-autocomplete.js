
jQuery(document).ready(function($){
  
  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: search_list,
    onSelect: function (suggestion) {
      nodeClicked(suggestion.value); // pass the node id
    }
  });
  

});