from src.views.http_types.http_response import HttpResponse

def hander_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "titles": "Server error",
                "detail": str(error)

            }]
            
        }
    )