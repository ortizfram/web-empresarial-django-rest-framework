import FullWithLayout from "hocs/layouts/FullWithLayout";
import { connect } from "react-redux";
import React from "react";
import { get_blog_list, get_blog_list_page } from "redux/actions/blog";
import { useEffect } from "react";
import LoadingCard from "components/loaders/LoadingCard";
import BlogCard from "./BlogCard";
import CategoriesSmallSetPagination from "components/pagination/CategoriesSmallSetPagination";
import { Link } from "react-router-dom";

function BlogList({ get_blog_list_page, blog_list, count, category_id }) {
  useEffect(() => {
    get_blog_list();
  }, []);

  return (
    <div>
      {blog_list ? (
        <>
          <div className="relative bg-gray-50 pb-8 px-4 sm:px-6 lg:pb-12 lg:px-8">
            <div className="absolute inset-0">
              <div className="bg-white h-1/3 sm:h-2/3" />
            </div>
            <div className="relative max-w-7xl mx-auto">
              <Link
                to="/blog"
                className="mt- 4 text-sm font-semibold text-indigo-600 hover:text-indigo-500 sm:block"
              >
                Browse all categories<span aria-hidden="true"> &rarr;</span>
              </Link>
              <div className="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">
                {blog_list.map((post) => (
                  <BlogCard data={post} />
                ))}
              </div>
              <CategoriesSmallSetPagination
                get_blog_list_page={get_blog_list_page}
                blog_list={blog_list}
                count={count}
                category_id={category_id}
              />
            </div>
          </div>
        </>
      ) : (
        <div className="relative bg-gray-50 pb-8 px-4 sm:px-6 lg:pb-12 lg:px-8">
          <div className="absolute inset-0">
            <div className="bg-white h-1/3 sm:h-2/3" />
          </div>
          <div className="relative max-w-7xl mx-auto">
            <Link
              to="/blog"
              className="mt- 4 text-sm font-semibold text-indigo-600 hover:text-indigo-500 sm:block"
            >
              Browse all categories<span aria-hidden="true"> &rarr;</span>
            </Link>
            <div className="mt-12 max-w-lg mx-auto grid gap-5 lg:grid-cols-3 lg:max-w-none">
              <LoadingCard />
            </div>
            <CategoriesSmallSetPagination
              get_blog_list_page={get_blog_list_page}
              blog_list={blog_list}
              count={count}
              category_id={category_id}
            />
          </div>
        </div>
      )}
    </div>
  );
}

const mapStateToProps = (state) => ({});

export default connect(mapStateToProps, {})(BlogList);
