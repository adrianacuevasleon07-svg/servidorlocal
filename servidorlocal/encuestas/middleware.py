class CapturarPeticionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__ (self, request):
        metodo = request.method
        ruta = ruta = request.path # Captura la URL (ej: /encuestas/)

        # Imprime la información en la consola de tu terminal
        print(f"\n[INFO] Cliente solicita: {metodo} -> {ruta}")

        # Ejecuta la vista y obtiene la respuesta
        response = self.get_response(request)

        # 2. Código que se ejecuta DESPUÉS de la vista (opcional):
        # Aquí podrías ver el estatus de la respuesta (ej: 200 OK, 404 Not Found)
        print(f"[INFO] Respuesta enviada con código: {response.status_code}")

        return response
            
                