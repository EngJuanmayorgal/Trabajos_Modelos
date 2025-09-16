package Servlets;

import Fabrica.FabricaAbstracta;
import Fabrica.FabricaElfos;
import Fabrica.FabricaEnanos;
import Fabrica.FabricaHumanos;
import Fabrica.FabricaOrcos;
import java.io.IOException;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import org.json.JSONArray;
import org.json.JSONObject;

@WebServlet(name = "EscogerServlet", urlPatterns = {"/EscogerServlet"})
public class EscogerPersonajes extends HttpServlet {

    public FabricaAbstracta f;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String type = request.getParameter("type");
        response.setContentType("application/json");
        response.setCharacterEncoding("UTF-8"); 

        JSONObject character = new JSONObject();

        if ("humano".equalsIgnoreCase(type)) {
            f = new FabricaHumanos();
            character.put("img", f.getCuerpo().getImg());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getMontura().montura()));
            character.put("parts", parts);
        } else if ("elfo".equalsIgnoreCase(type)) {
            f = new FabricaElfos();
            character.put("img", f.getCuerpo().getImg());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getMontura().montura()));
            character.put("parts", parts);
        } else if ("enano".equalsIgnoreCase(type)) {
            f = new FabricaEnanos();
            character.put("img", f.getCuerpo().getImg());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getMontura().montura()));
            character.put("parts", parts);
        } else if ("orco".equalsIgnoreCase(type)) {
            f = new FabricaOrcos();
            character.put("img", f.getCuerpo().getImg());
            JSONArray parts = new JSONArray();
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArma().arma()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getArmadura().armadura()));
            parts.put(new JSONObject().put("img", f.getArma().getImg()).put("info", f.getMontura().montura()));
            character.put("parts", parts);
        } else {
            character.put("img", "");
            character.put("parts", new JSONArray());
        }

        response.getWriter().write(character.toString());
    }
}
