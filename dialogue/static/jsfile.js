/**
 * Created by Alireza on 5/14/17.
 */
function save_movie(input_id){
    $.ajax({
        url : "/dialogue/polls/dialogues/"+input_id,
        success: function(data1){
            if(data1['status'] == 'ok'){
                var text = 'Movie ' +data1['movie_name']+ ' added Successfully';
                $('#response').html(text);
                $('#response').addClass('btn-success');
                $('#response').removeClass('btn-danger');
            }
            else{
                $('#response').html('Movie Adding Failed!');
                $('#response').removeClass('btn-success');
                $('#response').addClass('btn-danger');
            }
        }
    })
}
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
                        var text_data = '<div class="col-md-4"> <div class="movie_div"><div class="title_div"> <h6 class="title_header" style="">'+data1.Search[index].Title+'</h6> </div> <div class="row"> <div class="col-md-6"> <a href="http://im.tinymdb.com/title/'+data1.Search[index].imdbID+'"><img class="movie_image" src="'+ data1.Search[index].Poster +'" alt="'+data1.Search[index].Title+'"></a></div><div class="col-md-6"> <div class="div_info"> <div class="more_information">Year : '+data1.Search[index].Year+'</div> </div> <div class="div_movie_page"> <div class="movie_page"><a href="http://im.tinymdb.com/title/'+data1.Search[index].imdbID+'">Visit Movie Page</a></div> </div> <div class="div_movie_page"> <div class="add_movie"><button class="add_movie" onclick="save_movie(\''+data1.Search[index].imdbID+'\')">Add Movie</button></div> </div> </div> </div> <hr style="color:white"> </div> </div>';
                        $('#result_search').append(text_data);
                 });
            }
        });
});
})
function send_dialogue(p,id_input){
    $.get( "/dialogue/polls/getGet/", { p: p , imdb_id : id_input } );
    var text = '<div class="col-md-3"> <div class="dialogue_st" style="margin:10px;padding:10px;"> <p>Dialogue Text</p> <hr> '+p+'</div> </div>'
    $('#dialogue_div').append(text);
}