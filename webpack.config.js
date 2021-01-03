const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  devtool: 'eval-source-map',
  entry: './flaskr/static/js/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, './flaskr/static/dist'),
    assetModuleFilename: './flaskr/static/images/[name].[ext]'
  },
    devServer: {
        contentBase: './flaskr/static/dist',
      },
    module: {
        rules: [
            {
            // scss loader
            test: /\.scss$/,
            use: [
                // MINICSSPLUGIN: generate a style.css file inside dist folder with better performance (not through js). I added the public path because of an error
                {
                    loader: MiniCssExtractPlugin.loader,
                    options : {
                        publicPath:"./flaskr/static/js"
                    },
                },
                {
                    loader: "css-loader",
                },
                {
                    loader: "sass-loader",
                }
            ],
            },
            {
              test: /\.js$/,
              exclude: /node_modules/,
              use: ["babel-loader"]
            },
            {
              test: /\.html$/i,
              loader: 'html-loader',
              options: {
                attributes: {
                  list: [
                    {
                      tag: 'img',
                      attribute: 'src',
                      type: 'src',
                    },
                  ]
                }
              }
            },
            { 
                // fonts loader
                test: /\.(woff|woff2|eot|ttf)$/,
                type: 'asset/resource'
              },
            // video
          // images asset/resouce: take all the images and put them to destination folder images
          { 
            test: /\.(webp)$/i,
            type:"asset/resource",
            generator: {
              filename: 'images/[name].[ext]'
            }
          },
          { test: /\.(png|svg|jpg|gif|webm|mp4)$/,
            use: [
            {
              loader: 'file-loader',
              options: {
                esModule: false,
                name: "[name].[ext]",
                outputPath: "images/",
                publicPath: "images/",
              } 
            }
            ]
          },
        ]
    },
    plugins: [
          new HtmlWebpackPlugin({
            filename: "index.html", 
            template: path.resolve(__dirname, "flaskr","templates","auth", "index.html")
          }),
          new HtmlWebpackPlugin({
            filename: "landing-page.html",
            template: path.resolve(__dirname, "flaskr","templates","upload", "landing_page.html")
          }),
        new MiniCssExtractPlugin({
            filename: "style.css"
          }),
    ]
};