import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  	distDir: 'build',
	rewrites: async () => {
		return [
			{
				source: '/api/:path*',
				destination: `http://${process.env.PROXY_HOST}:${process.env.PROXY_PORT}/api/:path*`
			}
		]
	}
};

export default nextConfig;
