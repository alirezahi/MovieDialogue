/**
 * Created by Alireza on 5/14/17.
 */
$(document).ready(function(){
    $("button").click(function(){
    $.ajax({
            url: "http://www.omdbapi.com/?",
            data: {
                "s":$('#movie_name_input').val()
            },
            success: function (data1) {
                $('#result_search').html('');
                $.each(data1.Search, function(index) {
                        var text_data = '<div class="col-md-4"> <div class="movie_div"><div class="title_div"> <h6 class="title_header" style="">'+data1.Search[index].Title+'</h6> </div> <div class="row"> <div class="col-md-6"> <a href="http://im.tinymdb.com/title/'+data1.Search[index].imdbID+'"><img class="movie_image" src="'+ data1.Search[index].Poster +'" alt="'+data1.Search[index].Title+'"></a></div><div class="col-md-6"> <div class="div_info"> <div class="more_information">Year : '+data1.Search[index].Year+'</div> </div> <div class="div_movie_page"> <div class="movie_page"><a href="http://im.tinymdb.com/title/'+data1.Search[index].imdbID+'">Visit Movie Page</a></div> </div> <div class="div_movie_page"> <div class="add_movie"><a href="/dialogue/polls/dialogues/'+data1.Search[index].imdbID+'">Add Movie</a></div> </div> </div> </div> <hr style="color:white"> </div> </div>';
                        $('#result_search').append(text_data);
                 });
            }
        });
});
})
function send_dialogue(p,id_input){
    $.get( "/dialogue/polls/getGet/", { p: p , imdb_id : id_input } )
}