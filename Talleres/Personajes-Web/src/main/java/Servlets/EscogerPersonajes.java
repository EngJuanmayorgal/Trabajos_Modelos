package Servlets;

/**
 *
 * @author Juan Mayorga, Mariam, Samuel
 */

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONArray;
import org.json.JSONObject;

import Fabrica.FabricaAbstracta;
import Fabrica.FabricaElfos;
import Fabrica.FabricaEnanos;
import Fabrica.FabricaHumanos;
import Fabrica.FabricaOrcos;

@WebServlet(name = "EscogerServlet", urlPatterns = {"/EscogerServlet"})
public class EscogerPersonajes extends HttpServlet {

    // Fábrica abstracta que permitirá instanciar la raza seleccionada
    public FabricaAbstracta f;

    /**
     * Método que responde a las solicitudes GET.Recibe un parámetro "type"
     * (humano, elfo, enano u orco).Según el valor, instancia la fábrica
     * correspondiente, construye el personaje con sus partes y devuelve un JSON
     * con la información del personaje (nombre, imagen y descripción).
     *
     * @param request
     * @param response
     * @throws javax.servlet.ServletException
     * @throws java.io.IOException
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Se obtiene el tipo de personaje que se solicita
        String type = request.getParameter("type");
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8");

        // Objeto JSON que contendrá toda la información del personaje
        JSONObject character = new JSONObject();

        // Dependiendo del tipo de personaje, se crea la fábrica adecuada
        if ("humano".equalsIgnoreCase(type)) {
            f = new FabricaHumanos();
            // Se arma el JSON con sus partes
            character.put("img", f.getCuerpo().getImg());
            character.put("name", f.getCuerpo().getName());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArmadura().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getMontura().getImg()).put("info", f.getMontura().montura()));
            parts.put(new JSONObject().put("img", f.getCuerpo().getImg()).put("info", f.getCuerpo().stats()));
            character.put("parts", parts);
        } else if ("elfo".equalsIgnoreCase(type)) {
            f = new FabricaElfos();
            character.put("img", f.getCuerpo().getImg());
            character.put("name", f.getCuerpo().getName());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArmadura().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getMontura().getImg()).put("info", f.getMontura().montura()));
            parts.put(new JSONObject().put("img", f.getCuerpo().getImg()).put("info", f.getCuerpo().stats()));
            character.put("parts", parts);
        } else if ("enano".equalsIgnoreCase(type)) {
            f = new FabricaEnanos();
            character.put("img", f.getCuerpo().getImg());
            character.put("name", f.getCuerpo().getName());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArmadura().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getMontura().getImg()).put("info", f.getMontura().montura()));
            parts.put(new JSONObject().put("img", f.getCuerpo().getImg()).put("info", f.getCuerpo().stats()));
            character.put("parts", parts);
        } else if ("orco".equalsIgnoreCase(type)) {
            f = new FabricaOrcos();
            character.put("img", f.getCuerpo().getImg());
            character.put("name", f.getCuerpo().getName());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArmadura().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getMontura().getImg()).put("info", f.getMontura().montura()));
            parts.put(new JSONObject().put("img", f.getCuerpo().getImg()).put("info", f.getCuerpo().stats()));
            character.put("parts", parts);
        } else {
            // Si el tipo no coincide con ninguna raza, se retorna vacío
            character.put("img", "");
            character.put("parts", new JSONArray());
        }

        // Se envía la respuesta en formato JSON al cliente
        response.getWriter().write(character.toString());
    }
}
