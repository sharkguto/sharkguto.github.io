module.exports = {
  chainWebpack: (config) => {
    config.resolve.symlinks(false);
  },
  // configureWebpack: {
  //   optimization: {
  //     splitChunks: false,
  //   },
  //   css: {
  //     extract: false,
  //   },
  // },
};
