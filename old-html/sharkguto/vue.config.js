

module.exports = {
  configureWebpack: {
    optimization: {
      splitChunks: false,
      moduleIds: false,
    },
  },
  css: {
    extract: false, // true if separate css
  },


};
