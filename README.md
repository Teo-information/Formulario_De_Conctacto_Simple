# Formulario de Contacto Simple

Este proyecto es un formulario de contacto moderno y responsivo, desarrollado para la gestión eficiente de mensajes de usuarios. Incluye validación de campos en el frontend con JavaScript y simula el almacenamiento de mensajes mediante una API REST local utilizando [json-server](https://github.com/typicode/json-server).

## Características

- **Validación de campos**: Todos los campos son validados en el navegador antes de enviar.
- **Confirmación visual**: El usuario recibe una notificación visual tras el envío exitoso.
- **Simulación de API REST**: Los mensajes se almacenan en un archivo JSON local usando json-server.
- **Diseño responsivo y soporte para dark mode**.
- **Código estructurado y fácil de mantener**.

## Estructura del Proyecto

```
/
├── db.json
├── formulario.html
├── style.css
├── validacion.js
└── README.md
```

## Requisitos

- [Node.js](https://nodejs.org/)
- [json-server](https://github.com/typicode/json-server)

## Instalación y Ejecución

1. **Clona el repositorio:**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd Formulario_De_Conctacto_Simple
   ```

2. **Instala json-server (si no lo tienes):**
   ```sh
   npm install -g json-server
   ```

3. **Inicia el servidor simulado:**
   ```sh
   json-server --watch db.json --port 3001
   ```

4. **Abre `index.html` en tu navegador favorito.**

## Uso

- Completa el formulario y haz clic en "Enviar".
- El mensaje será validado y almacenado en `db.json` a través de la API REST simulada.
- Se mostrará una confirmación visual si el envío es exitoso.

## Personalización

- Puedes modificar los campos del formulario en `index.html`.
- El estilo puede ajustarse desde `style.css`.
- La lógica de validación y envío está en `validacion.js`.

## Soporte

Para reportar problemas o sugerir mejoras, abre un [issue](https://github.com/tuusuario/Formulario_De_Conctacto_Simple/issues).

---

© 2025 Reflexo. Proyecto de ejemplo usando la metologia scrum.
