/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
}

module.exports = nextConfig;

module.exports = {
  env: {
    BITLY_API_KEY: process.env.BITLY_API_KEY,
  }
}
