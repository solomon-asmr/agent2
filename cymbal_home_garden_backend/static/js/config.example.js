// Production configuration file
// Copy this to config.js and update values for your production environment

const CONFIG = {
  // Backend API configuration
  BACKEND_URL: "https://your-domain.com",
  API_BASE_URL: "https://your-api-domain.com/api",

  // WebSocket configuration
  WEBSOCKET_BASE_URL: "wss://your-websocket-domain.com",

  // Agent widget configuration
  WIDGET_ORIGIN: "https://your-domain.com",

  // Development/Production mode
  IS_DEVELOPMENT: false,

  // Enable debug logging (set to false for production)
  DEBUG_MODE: false,
};

// Export for use in other files
if (typeof module !== "undefined" && module.exports) {
  module.exports = CONFIG;
} else {
  window.CONFIG = CONFIG;
}
